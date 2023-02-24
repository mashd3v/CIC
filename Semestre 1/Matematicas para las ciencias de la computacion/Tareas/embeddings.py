'''
    Embeddings
    Asignatura: Matemáticas para las ciencias de la computación
    Alumno: Miguel Angel Soto Hernandez
'''

'''
NOTA IMPORTANTE: Es necesario instalar estos dos paquetes antes de ejecutar el codigo:

    pip install mxnet
    pip install d2l

Una vez instalados, deberan desaparecer los errores de importaciones
Si es asi, simplemente correr el archivo .py con el siguiente comando:
    
    python3 embeddings.py
'''

'''
Leemos y pre-procesamos el conjunto de datos
Este conjunto de datos ya ha sido preprocesado. Cada línea del conjunto de datos actúa como una frase. 
Todas las palabras de una frase están separadas por espacios. 
En la tarea de incrustación de palabras, cada palabra es un token.
'''
def read_ptb():
    data_dir = d2l.download_extract('ptb')
    with open(os.path.join(data_dir, 'ptb.train.txt')) as f:
      raw_text = f.read()

    return [line.split() for line in raw_text.split('\n')]

'''
Submuestreo
En los datos de texto, generalmente hay algunas palabras que aparecen con alta frecuencia, como "the", 
"a" y "in" en inglés. En general, en una ventana de contexto, es mejor entrenar el modelo de incrustación 
de palabras cuando una palabra (como "chip") y una palabra de menor frecuencia (como "microprocesador") 
aparecen al mismo tiempo, que cuando una palabra aparece con otra de mayor frecuencia (como "the"). 
Por lo tanto, al entrenar el modelo de incrustación de palabras, podemos realizar un submuestreo de 
las palabras (Mikolov et al., 2013b).

Aquí, f(wi) es la relación entre las instancias de la palabra wi y el número total de palabras en el 
conjunto de datos, y la constante t es un hiperparámetro (fijado en 10-4 en este experimento). Como podemos 
ver, sólo es posible posible descartar la palabra wi en el submuestreo cuando f(wi) > t. Cuanto mayor sea la 
frecuencia de la palabra mayor es la probabilidad de que la palabra sea eliminada.
'''
def subsampling(sentences, vocab):
    # Mapear palabras de frecuencias bajas en <unk>
    sentences = [[vocab.idx_to_token[vocab[tk]] for tk in line] for line in sentences]
    # Contar la frecuencia de cada palabra
    counter = d2l.count_corpus(sentences)
    num_tokens = sum(counter.values())
    # Regresa verdadero si mantendra el token durante el submuestreo
    def keep(token):
      return (random.uniform(0, 1) < math.sqrt(1e-4 / counter[token] * num_tokens))
    # Ahora, haz el submuestreo
    return [[tk for tk in line if keep(tk)] for line in sentences]

# Para los tokens individuales, la frecuencia de muestreo de la palabra de alta frecuencia "el" es inferior a 1/20.
def compare_counts(token):
    return (f'Numero del token "{token}": '
      f'antes={sum([line.count(token) for line in sentences])}, '
      f'despues={sum([line.count(token) for line in subsampled])}')


'''
Cargando el conjunto de datos
Extracción de palabras objetivo centrales y palabras de contexto
Utilizamos las palabras cuya distancia a la palabra central de destino no supera el tamaño de la ventana 
de contexto como palabras de contexto de la palabra objetivo central dada. La siguiente función de definición 
extrae todas las palabras objetivo centrales y sus palabras de contexto. Muestrea de manera uniforme y 
aleatoria un número entero para como tamaño de la ventana de contexto entre el entero 1 y el max_window_size 
(ventana de contexto máxima). ventana de contexto).
'''
def get_centers_and_contexts(corpus, max_window_size):
    centers, contexts = [], []
    for line in corpus:
        # Cada oracion necesita al menos 2 palabras para que tengamos la forma:
        # Palabra central - Palabra de contexto como par
        if len(line) < 2:
            continue
        centers += line
        # Ventana de contexto centrada en i
        for i in range(len(line)):
            window_size = random.randint(1, max_window_size)
            indices = list(range(max(0, i - window_size),
                                 min(len(line), i + 1 + window_size)))
            # Excluir la palabra central de las palabras de contexto
            indices.remove(i)
            contexts.append([line[idx] for idx in indices])
    return centers, contexts


'''
Muestreo negativo
Utilizamos el muestreo negativo para el entrenamiento aproximado. Para un par de palabras centrales y de contexto, 
muestreamos aleatoriamente K palabras con ruido (K = 5 en el experimento). De acuerdo con la sugerencia del 
documento Word2vec, la probabilidad de muestreo de palabras con ruido P(w) es la relación entre la frecuencia 
de palabras de w a la frecuencia total de palabras elevada a la potencia de 0,75 (Mikolov et al., 2013b). En 
primer lugar, definimos una clase para extraer un candidato en función de los pesos de muestreo. Se almacena 
en caché un banco de números aleatorios de 10000 en lugar de llamar a random.choices cada vez.
'''
class RandomGenerator:
    # Dibujar un entero random en [0, n] de acuerdo a los pesos de las n muestras
    def __init__(self, sampling_weights):
        self.population = list(range(len(sampling_weights)))
        self.sampling_weights = sampling_weights
        self.candidates = []
        self.i = 0

    def draw(self):
        if self.i == len(self.candidates):
            self.candidates = random.choices(self.population,
                                           self.sampling_weights, k=10000)
            self.i = 0
        self.i += 1
        return self.candidates[self.i - 1]


def get_negatives(all_contexts, corpus, K):
    counter = d2l.count_corpus(corpus)
    sampling_weights = [counter[i]**0.75 for i in range(len(counter))]
    all_negatives, generator = [], RandomGenerator(sampling_weights)
    for contexts in all_contexts:
        negatives = []
        while len(negatives) < len(contexts) * K:
            neg = generator.draw()
            # Palabras ruido no pueden ser palabras de contexto
            if neg not in contexts:
                negatives.append(neg)
        all_negatives.append(negatives)
    return all_negatives

'''
Lectura en lotes
Extraemos todas las palabras objetivo centrales all_centers, y las palabras de contexto all_contexts y 
las palabras de ruido de cada palabra central del conjunto de datos. Las leeremos en minilotes aleatorios al azar.

En un minilote de datos, el i ejemplo incluye una palabra central y sus correspondientes ni palabras de contexto 
y mi palabras de ruido. Dado que el tamaño de la ventana de contexto de cada ejemplo puede ser diferente, la suma 
de palabras de contexto y palabras de ruido, ni + mi será diferente. Al construir un Cuando se construye un minilote,
 se concatenan las palabras de contexto y las palabras de ruido de cada ejemplo, y se añaden 0s para hasta que 
 la longitud de las concatenaciones sea la misma, es decir, que la longitud de todas las concatenaciones sea 
 maxi ni + mi(max_len). Para evitar el efecto del relleno en el cálculo de la función de pérdida construimos 
 la variable de máscara máscaras, cada elemento de la cual corresponde a un elemento de la concatenación de 
 palabras de contexto y ruido, contextos_negativos. Cuando un elemento Cuando un elemento de la variable 
 contextos_negativos es un relleno, el elemento de la variable máscara en la misma posición será 0. misma posición 
 será 0. En caso contrario, toma el valor 1. Para distinguir entre ejemplos positivos y negativos, también tenemos 
 que distinguir las palabras de contexto de las palabras de ruido en la variable contextos_negativos. Basándonos 
 en la construcción de la variable máscara, sólo necesitamos crear una variable label con la misma forma que la 
 variable contexts_negatives y establecer los elementos correspondientes a las palabras de contexto (ejemplos 
 positivos) a 1, y el resto a 0.

A continuación, implementaremos la función de lectura de minilotes batchify. Los datos de entrada del minilote 
son una lista lista cuya longitud es el tamaño del lote, cada elemento de la cual contiene palabras centrales 
de destino palabras de contexto contexto, y palabras de ruido negativo. Los datos del minilote devueltos por 
esta función se ajusta al formato que necesitamos, por ejemplo, incluye la variable de máscara.
'''
def batchify(data):
    max_len = max(len(c) + len(n) for _, c, n in data)
    centers, contexts_negatives, masks, labels = [], [], [], []
    for center, context, negative in data:
        cur_len = len(context) + len(negative)
        centers += [center]
        contexts_negatives += [context + negative + [0] * (max_len - cur_len)]
        masks += [[1] * cur_len + [0] * (max_len - cur_len)]
        labels += [[1] * len(context) + [0] * (max_len - len(context))]
    return (np.array(centers).reshape((-1, 1)), np.array(contexts_negatives),
            np.array(masks), np.array(labels))

'''
Poniendo todo junto
Por último, definimos la función load_data_ptb que lee el conjunto de datos PTB y devuelve el iterador de datos.
'''
def load_data_ptb(batch_size, max_window_size, num_noise_words):
    num_workers = d2l.get_dataloader_workers()
    sentences = read_ptb()
    vocab = d2l.Vocab(sentences, min_freq=10)
    subsampled = subsampling(sentences, vocab)
    corpus = [vocab[line] for line in subsampled]
    all_centers, all_contexts = get_centers_and_contexts(corpus, max_window_size)
    all_negatives = get_negatives(all_contexts, corpus, num_noise_words)
    dataset = gluon.data.ArrayDataset(all_centers, all_contexts, all_negatives)
    data_iter = gluon.data.DataLoader(dataset, batch_size, shuffle=True, 
                                      batchify_fn=batchify, num_workers=num_workers)
    return data_iter, vocab


'''
Cálculo de los modelos de saltos de línea hacia delante
En el cálculo hacia adelante, la entrada del modelo de diagrama saltado contiene el índice central de la 
palabra objetivo y el índice concatenado de contextos y palabras de ruido contextos_y_negativos. En el cual, 
la variable centro tiene la forma (tamaño del lote, 1), mientras que la variable contextos_y_negativos tiene 
la forma (tamaño del lote, max_len). Estas dos variables se transforman primero de índices de palabras a vectores 
de palabras mediante la capa de incrustación de palabras, y luego la salida de la forma (tamaño del lote, 1, max_len) 
se obtiene mediante la multiplicación de minilotes. Cada elemento de la salida es el producto interno del vector de 
palabras objetivo central y el vector de palabras de contexto o el vector de palabras de ruido.
'''
def skip_gram(center, contexts_and_negatives, embed_v, embed_u):
    v = embed_v(center)
    u = embed_u(contexts_and_negatives)
    pred = npx.batch_dot(v, u.swapaxes(1, 2))
    return pred


'''
Entrenamiento
La función de entrenamiento se define a continuación. Debido a la existencia de relleno, el cálculo de la función 
de pérdida función de pérdida es ligeramente diferente en comparación con las funciones de entrenamiento anteriores.
'''    
def train(net, data_iter, lr, num_epochs, device=d2l.try_gpu()):
    net.initialize(ctx=device, force_reinit=True)
    trainer = gluon.Trainer(net.collect_params(), 'adam', {'learning_rate': lr})
    animator = d2l.Animator(xlabel='epoch', ylabel='loss', xlim=[1, num_epochs])
    metric = d2l.Accumulator(2) # Sum of losses, no. of tokens
    
    for epoch in range(num_epochs):
        timer, num_batches = d2l.Timer(), len(data_iter)
        
        for i, batch in enumerate(data_iter):
        center, context_negative, mask, label = [data.as_in_ctx(device) for data in batch]
        
        with autograd.record():
            pred = skip_gram(center, context_negative, net[0], net[1])
            l = (loss(pred.reshape(label.shape), label, mask) / mask.sum(axis=1) * mask.shape[1])
        
        l.backward()
        trainer.step(batch_size)
        metric.add(l.sum(), l.size)
        if (i + 1) % (num_batches // 5) == 0 or i == num_batches - 1:
            animator.add(epoch + (i + 1) / num_batches, (metric[0] / metric[1],))
    
    print(f'loss {metric[0] / metric[1]:.3f}, 'f'{metric[1] / timer.stop():.1f} tokens/sec on {str(device)}')

'''
Aplicación del modelo de incrustación de palabras
'''
def get_similar_tokens(query_token, k, embed):
    W = embed.weight.data()
    x = W[vocab[query_token]]
    # Compute the cosine similarity. Add 1e-9 for numerical stability
    cos = np.dot(W, x) / np.sqrt(np.sum(W * W, axis=1) * np.sum(x * x) + 1e-9)
    topk = npx.topk(cos, k=k + 1, ret_typ='indices').asnumpy().astype('int32')
    for i in topk[1:]: # Remove the input words
        print(f'cosine sim={float(cos[i]):.3f}: {vocab.idx_to_token[i]}')


if __name__ == '__main__':
    # Importamos los paquetes y modulos requeridos para el ejemplo
    import math
    import os
    import random
    from mxnet import gluon, np
    from d2l import mxnet as d2l

    d2l.DATA_HUB['ptb'] = (d2l.DATA_URL + 'ptb.zip',
                       '319d85e578af0cdc590547f26231e4e31cdf1e42')

    # Ejecucicion e impresion de la funcion read_ptb()
    sentences = read_ptb()
    print(f'Numero de oraciones: {len(sentences)}') 

    '''
    A continuación construimos un vocabulario con palabras que aparecen no más de 10 veces mapeadas en un 
    <unk> ...en un token <unk>. Obsérvese que los datos preprocesados de la OPA también contienen tokens 
    <unk> que presentan palabras raras.
    '''
    vocab = d2l.Vocab(sentences, min_freq=10)
    print(f'Tamano del vocabulario: {len(vocab)}')

    # Submuestreo
    subsampled = subsampling(sentences, vocab)

    # Comparar conteo
    compare_counts('the')

    # Asignamos cada token a un indice para construir un corpus
    corpus = [vocab[line] for line in subsampled]

    '''
    A continuación, creamos un conjunto de datos artificial que contiene dos frases de 7 y 3 palabras, 
    respectivamente. Supongamos que la ventana de contexto máxima es 2 e imprimamos todas las palabras 
    centrales de destino y sus palabras de contexto palabras.
    '''
    tiny_dataset = [list(range(7)), list(range(7, 10))]
    print('Dataset', tiny_dataset)

    for center, context in zip(*get_centers_and_contexts(tiny_dataset, 2)):
        print('Central', center, 'Tiene contextos', context)

    # Fijamos el tamaño máximo de la ventana de contexto en 5. A continuación se extraen todas las palabras 
    # objetivo centrales y sus palabras de contexto en el conjunto de datos.
    all_centers, all_contexts = get_centers_and_contexts(corpus, 5)
    print(f'Numero de parejas de palabras centrales-context: {len(all_centers)}')

    # Muestreo negativo
    generator = RandomGenerator([2, 3, 4])
    [generator.draw() for _ in range(10)]
    all_negatives = get_negatives(all_contexts, corpus, 5)

    # Lectura por lotes
    x_1 = (1, [2, 2], [3, 3, 3, 3])
    x_2 = (1, [2, 2, 2], [3, 3])
    batch = batchify((x_1, x_2))
    names = ['centers', 'contexts_negatives', 'masks', 'labels']

    for name, data in zip(names, batch):
        print(name, '=', data)
    # Utilizamos la función batchify que acabamos de definir para especificar el método de lectura del minilote 
    # en la instancia de DataLoader.
    
    # Imprimamos el primer minilote del iterador de datos.
    data_iter, vocab = load_data_ptb(512, 5, 5)
    for batch in data_iter:
        for name, data in zip(names, batch):
            print(name, 'shape:', data.shape)
        break

    # Pre- entrenando word2vec
    from mxnet import autograd, gluon, np, npx
    from mxnet.gluon import nn
    from d2l import mxnet as d2l
    npx.set_np()
    batch_size, max_window_size, num_noise_words = 512, 5, 5
    data_iter, vocab = d2l.load_data_ptb(batch_size, max_window_size, 
                                        num_noise_words)

    '''
    Implementaremos el modelo de salto de grama mediante el uso de capas de incrustación y la multiplicación 
    de minilotes. Estos métodos también se utilizan a menudo para implementar otras aplicaciones de procesamiento 
    del lenguaje natural.
    '''
    embed = nn.Embedding(input_dim=20, output_dim=4)
    embed.initialize()
    embed.weight

    '''
    La entrada de la capa de incrustación es el índice de la palabra. Cuando introducimos el índice i de una 
    palabra, la capa de incrustación devuelve la fila i de la matriz de pesos como su vector de palabras. A 
    continuación introducimos un índice de forma (2, 3) en la capa de incrustación. Como la dimensión del vector 
    de palabras es 4, obtenemos un vector de palabras de forma (2, 3, 4).
    '''                              
    x = np.array([[1, 2, 3], [4, 5, 6]])
    embed(x)

    # Verificamos la forma de la salida, debe ser (tamaño del lote, max_len)
    skip_gram(np.ones((2, 1)), np.ones((2, 4)), embed, embed).shape

    '''
    Función de pérdida de entropía cruzada binaria
    De acuerdo con la definición de la función de pérdida en el muestreo negativo, podemos utilizar directamente 
    la función de pérdida de entropía cruzada binaria desde las API de alto nivel.
    '''
    loss = gluon.loss.SigmoidBCELoss()

    '''
    Cabe mencionar que podemos utilizar la variable de máscara para especificar el valor predicho parcial y 
    la etiqueta que participan en el cálculo de la función de pérdida en el minilote: cuando la máscara es 1,
    el valor predicho y la etiqueta de la posición correspondiente participarán en el cálculo de la función de 
    pérdida; cuando la máscara es 0, no participan. Como hemos mencionado anteriormente, las variables de máscara 
    pueden utilizarse para evitar el efecto del relleno en los cálculos de la función de pérdida.
    Dados dos ejemplos idénticos, diferentes máscaras conducen a diferentes valores de pérdida.
    '''
    pred = np.array([[.5] * 4] * 2)
    label = np.array([[1., 0., 1., 0.]] * 2)
    mask = np.array([[1, 1, 1, 1], [1, 1, 0, 0]])
    loss(pred, label, mask)

    # Podemos normalizar la perdida en cada ejemplo debido a las diferentes longitudes en cada ejemplo.
    loss(pred, label, mask) / mask.sum(axis=1) * mask.shape[1]

    # Construimos las capas de incrustación de las palabras centrales y de contexto, respectivamente, 
    # y establecemos la dimensión del vector de palabras del hiperparámetro embed_size en 100.
    embed_size = 100
    net = nn.Sequential()
    net.add(nn.Embedding(input_dim=len(vocab), output_dim=embed_size), 
            nn.Embedding(input_dim=len(vocab), output_dim=embed_size))

    # Ahora podemos entrenar el modelo skip-gram usando muestreo negativo (puede tardar)
    lr, num_epochs = 0.01, 5
    train(net, data_iter, lr, num_epochs)

    '''
    Después de entrenar el modelo de incrustación de palabras, podemos representar la similitud de significado 
    entre las palabras basándonos en la similitud del coseno de dos vectores de palabras. Como podemos ver, al 
    utilizar el modelo de incrustación de palabras entrenado, las palabras más cercanas en significado a la palabra 
    "chip" están relacionadas en su mayoría con los chips.
    '''
    get_similar_tokens('chip', 3, net[0])
    

    
