---
marp: true
theme: uncover
paginate: true
math: true
backgroundColor: #fff
style: |
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
---

# Tutorial 1.2

Ahora que hemos simulado el modelo LIF, consideraremos la función de entrada y salida de este modelo

---

# Caracterización de la función de entrada-salida

Cada elemento de un circuito eléctrico se entiende en términos de su función entrada-salida. Por ejemplo, un transistor se entenderá en términos de la corriente que fluye a través de él en función del potencial entre las compuertas.

Si la neurona es la unidad computacional central, similar al transistor, ¿cuál es su función de entrada y salida? Bueno, esta es una pregunta bastante complicada porque realmente no sabemos cuál es la característica de entrada que se debe considerar y no sabemos realmente cuál es la característica de salida que se debe comunicar.

Sin embargo, este problema lo podemos simplificar un poco y de la gran cantidad de sinapsis que inciden en la célula y dan lugar a corrientes que luego desencadenan procesos en las dendritas, solo consideraremos las corrientes que fluyen desde las dendritas y las sinapsis, que se encuentran en el cuerpo celular que son los que más inmediatamente van a dar lugar a un potencial de acción. Entonces, considerarremos las características de esta corriente de entrada. Generalmente, su amplitud y cuanta corriente fluye. En cuanto a la salida, puede ser muchas características posibles de los trenes de picos de salida.

Entonces, el escenario más simpl es una condición en la que tenemos una entrada constante, una corriente constante $I$ que está estimulando la neurona. Si consideramos un modelo LIF donde esta corriente estimula cambios en el potencial de membrana hasta que alcanza un umbral donde el potencial de membrana se restablece, entonces las respuestas se verán un poco como la salida de la imagen. Y se ve que después de un periodo refractario absoluto, el potencial de membrana sigue una relajación hasta un estado estacionario y primero alcanza el umbral, emite un potencial de acción y se reinicia, y todo el proceso vuelve a empezar exactamente de la misma manera.

Una característica natural a tener en cuenta es el intervalo entre picos, la cantidad de tiempo entre dos picos ($|S|$). Esto tomando como inversa es la frecnuencia de disparo y hayq eu tener en cuenta que si tuvieramos que calcular el número de picos dentro de una ventana de tiempo bastante grande y dividir ese numero de picos por la longitud de esa ventana, también obtendríamos una frecuencia de disparo que sería exactamente equivalente a la inversa de la frecuencia de disparo. Entonces, esta frecuencia de disparo dependerá de la magnitud de la corriente que se inyecte. El disparo comenzará en algún punto donde la corriente sea lo suficientemente fuerte como para provocar un potencial de acción y luego seguirá una curva logarítmica (como se muestra en la imagen) que irá a una asíntota de 1 durante el periodo refractario absoluto. La curva se puede encontrar analíticamente con bastante facilidad a partir de las ecuaciones del modelo LIF y vemos que hay un logaritmo y depende de los parámetros del modelo, en particular de la corriente y la distancia al umbral.

Pero, ¿Qué pasa si además de esto hay ruido? Imaginemos que no solo una entrada media, sino que hay fluctuaciones que podrían tener que ver con le hecho de que no siempre hay exactamente la misma cantidad de entradas en cualquier momento estimulando esa neurona. Entoncesa agregamos ruido ($\xi$) al modelo LIF y la salida será bastante similar, pero más ruidosa. No se puede calcular el intervalo entre picos en un punto y llamarlo frecuencia, es necesario promediar varios picos, entonces, podemos tomar la inversa del intervalo promedio entre picos y si trazamos esto podremos ver que en ausencia de ruido tuvimos una transición brusca para iniciar una respuesta y una ganancia muy fuerte al inicio de la función de entrada-salida; y en presencia de ruido, la función de entrada-salida es mucho mayor, más lineal, es decir, el ruido está linealizando la función de entrada y salida. Otro aspecto importante es que en corrientes promedio que anteriormente no provocaban ninguna respuesta (que tienen amplitud media por debajo del umbral) pueden provocar una pequeña respuesta (una pequeña tasa de disparo), esto se debe a que estos picos están siendo impulsados por fluctuaciones aleatorias que resultan ser lo suficientemente fuertes como para provocar una respuesta y como son bastante frecuentes, se ve un a pequeña tasa de disparos. La ecuación analítica que describe esta curva también se conoce como ecuación de Siergert, esta hecho de función de error.

La corriente constante combinada con rido de fondo se puede entender en términos del intervsalo promedio entre picos en respuesta a esa entrada, pero esa no es toda la historia. El intervalo entre picos puede ser más o menos variable. Por ejemplo, en dos simulaciones diferentes del modelo LIF podemos ver que hay un caso en el que si hacemos el histograma de los diferentes intervalos entre picos, todos los intervalos están estrechamente centrados alrededor de la media, es decir, no son muy variables y es más o menos el mismo intervalo entre picos. Pero en el otro caso, es posible que se tenga un intervalo entre picos mucho más variable, y esto puede suceder en el mismo sentido, por lo que es posible que esta irregularidad se utilice para codificar. Entonces, lo que haremos es calcular el CV (Coeficiente de variación) que es simplemente una estadística natural en ese caso. El CV es solo la desviación estándar del intervalo entre picos entre la media, es decir, el intervalo medio entre picos.

En la misma situación que se ilustró anteriormente, donde la respuesta crecerá en función de la corriente promedio inyectada y donde podemos delimitar el área donde estaba por debajo del umbral en ausencia de ruido, podremos ver que el CV disminuirá con el promedio de la corriente inyectada y que por debajo de ese umbral el CV es notablemente superior. Esto ha llevado a la gente a hablar de dos regímenes. Tenemos el régimen impusado por fluctuaciones en el que la neurona no podría dispararse si no fuera por esas fluctuaciones y se asocia con un alto CV y una alta irregularidad; y luego este el régimen impulsado por la media, donde la neurona es impulsada principalmente por la media y la neurona se activa regularmente en un intervalo entre picos con una distribución muy estrecha.

Para concluir:

- La respuesta de la tasa de disparo de un modelo LIF es una función no lineal de la corriente que llega al cuerpo celular neuronal
- El ruido puede linealizar esta función de entrada-salida.
- La variabilida dde las respuestas no depende solo de la variabilidad de las entradas, sino que depende tanto de la media como de la varianza de las entradas
