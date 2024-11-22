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

# Tutorial 1.3

Aquí se explicarán algunas extensiones del modelo LIF que lo hacen más preciso.

---

# Generalized Integrate-and-Fire

Lo que no es una suposición tan buena fue ignorar los otros canales iónicos porque esos canales iónicos pueden regular fuertemente la dinámica de alcanzar el potencial de acción y, por lo tanto, cambiar si se ha generado o no un potencial de acción.

Entonces, lo que vamos a hacer es considerar una extensión de LIF que se llama **Generalized Integrate (GIF) o integración y fuego generalizados** y el enfoque aquí es reemplazar las complejas ecuaciones no lineales, que normalmente describirían las corrientes que fluyen desde los canales iónicos con ecuaciones lineales y que describen cuan preciso es esto.

Pero, ¿qué significa esto?

$$C_m \frac{dV}{dt} = -g_L (V - E_L) - \sum_k w_k + I$$

$$\text{Si } V = V_{th} \text{, entonces } V(t + \Delta) = E_L$$

Donde $a_k$ es acoplamiento subumbral de la k-ésima corriente y $\tau_k$ es la escala temporal de la k-ésima corriente.

Entonces, introduzcamos una $w$ actual que es un inhibidor, es decir, que cuando $w$ es positivo, $V$ tiende a disminuir. Se agrega una suma, que lo que significa es que puede haber múltiples corrientes con diferentes parámetros. Estos parámetros son: la escala de tiempo ($\tau$) y el acoplamiento con el potencial de membrana ($a$) que puede ser positivo o negativo. La corriente evolucionará siguiendo una dinámica lineal como puede verse en la ecuación diferencial ordinaria lineal ($a_k$). Y esto es a lo que llamamos una corriente lineal subumbral que introduce escalas de tiempo adicionales a la dinámica de la membrana

$$\tau_k \frac{d w_k}{dt} =  a_k (V - E_L) - w_k \text{ Corriente de subumbral linealizada}$$

Un ejemplo de tal efecto se puede ver en la siguiente imagen. Cuando se da un aumento escalonado en la corriente, en lugar de una relajación monoexponencial a un punto estacionario, se produce un sobreimpulso al que a veces le sigue incluso un subimpulso y luego llega al punto estacionario. Esta relajación no monoexponencial se debe a la corriente subumbral que está actuando exactamente en ese periodo de tiempo.

Mas importante ún, GIF también captura la adaptación de la frencuencia de pico. Entonces, la adaptación a la frecuencia de picos es es proceso por el cual las neuronas se adaptan a una determinada estimulación, lo que significa que el intervalo entre picos aumenta gradualmente con el tiempo cuando una entrada no cambia sino que permanece contante y estimulante. Esto se puede observar en la imagen de abajo, donde se tiene un paso de corriente por enciam del umbral y el intervalo entre picos está aumentando, lo cual se ve en casi todas las células, ya que casi todas las células muestran algún grado de adaptación a la frecuancia de picos.

El modelo LIF no puede reproducir esto, ya que siempre tendrá el mismo intervalo entre picos para una intendisdad de corriente de entrada determinada. Lo que podemos hacer es hacer que esta corriente de adaptación aumente, saltecada vez que haya un pico y luego seguir esta dinámica lineal y a eso lo llamamos un pico que provocó corriente.

Dentro del marco de las ecuaciones, agregamos esta corriente activada por pico a la condición de umbral, de modo que cada vez que alcanzamos un umbral y decimos que estamos emitiendo un pico no solo restablecemos el potencial de membrana a algún potencia $E_L$, sino que también damos un salto por $b_k$ y luego seguimos la misma dinámica. A esto es a lo que se le conoce como **corriente activada por pico linealizado**.

$$w_k (t + \Delta) = w_k + b_k$$

Donde $b_k$ es el salto provocado por un pico en la k-ésima corriente

Otro proceso que también es capaz de realizar una adaptación de la frecuencia de pico es el proceso en el que el umbral en sí es dinámico, de modo que cada vez que alcanzamos un pico, el umbral aumenta y puede decaer siguiendo una dinámica lineal. Esto se ve en las neuronas reales y las neuronas reales, al menos las excitadoras, muestran con mucha frecuencia este tipo de umbral de movimiento.

---

# Exactitud de modelos reducidos

Ahora, podemos probar la precisión de nuestro modelo y para hacerlo, inyectamos una corriente dependiente del tiempo en neuronas reales tomadas en porciones de la corteza. La neurona recibe una corriente de entrada que se parece mucho a la que recibiría normalmente _in vivo_. La respuesta son picos en el tiempo. El objetivo de nuestro modelo matemático de neuroas es predecir esos picos, es decir, utilizar el conocimiento de la corriente de entrada y parte de la respuesta para calibrar los parámetros del modelo y luego dejar que el modelo evolucione, dejar que aumente y probar si los tiempos de pico llegan a el lugar correcto. La métrica tendrá el tiempo de pico correcto más o menos $4ms$, después normalizamos ese número total de predicciones correctas del tiempo de pico mediante una medida de variabilidad intrínseca porque las neuronas no son perfectamente deterministas. Les damos la misma información varias veces y no siempre responderán al mismo tiempo, por lo que tendremos eso en cuenta.

Pero, ¿cómo es la comparación de modelos?

El modelo LIF, puede que no sea tan sorprendente, no es particularmente bueno para predecir las respuestas, ya que capturan el 40% de la variabilidad de la neurona. El GIF, teniendo en cuenta las características adaptativas está alcanzando el 80% en términos de precisión del modelo, lo cual es debido a que es un modelo mucho más complicado basado en la dinámica no lineal de los canales iónicos que se abren y cierran en la membrana celular, a esto se le llama **modelo Hodgkin-Huxley**. Hay que tener en cuenta que los resultados dependerán del tipo de célula paerticular que se utilizó para realizar el análisis. En este caso se hizo en células excitadoras. Entocnes, la mayor parte de la corteza estaá formada por células excitadoras. Si, en cambio, nos fijamos en las células inhibidoras, el modelo GIF captura el 100% de los tiempos de pico predecibles. Por lo tanto, podría decirse que es el modelo más simple que tiene la mayor precisión para esas células.

En general, lo que se deduce de todo esto es que las neuronas actúan aproximadamente como modelos LIF, pero los modelos GIF integran algunas características adaptativas y eso permite que este modelo capture sin mucha más complejidad el comportamiento de células reales

---
