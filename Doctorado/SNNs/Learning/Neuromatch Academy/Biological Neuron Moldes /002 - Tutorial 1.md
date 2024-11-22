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

# Tutorial 1

---

# Exitabilidad neuronal

Pasos del procesamiento de información:

- **Sinapsis:** conexión entre neuronas
- **Dendritas:** recibe las entradas
- **Cuerpo celular:** suma las corrientes de las dendritas y las sinapsis y toma la decisión de generar un potencial de acción
- **Axón:** envían los potenciales de acción

Cuando una entrada proviene de otras neuronas, primero para por las sinapsis, luego por las dendritas y luego va al cuerpo celular donde se toma la decisión de generar un potencial de acción.

Pero el tema de este tutorial se enfocará más en el cuerpo celular y de ¿cómo se genera un potencial de acción dada la corriente que fluye hacia el cuerpo celular desde las dendritas y las sinapsis? Por lo que nos enfocaremos en la excitabilidad de como y que genera el potencial de acción

---

# Descripción biológica

Si hacemos zoom en un área de la membrana, tenemos una corriente que posiblemente depende del tiempo y que incide en esa bicapa liídica. Esto influye en el potencial de membrana, que es la diferencia del potencial eléctrico entre el interior y el exterior de la célula.

Ahora podemos entender la relación entren la corriente y el potencial de membrana considerando la biofísica de la membrana como un circuito eléctrico. La bicapa liídica actúa como una capacitancia poruqe las cargas pueden acumularse a ambos lados de la membrana. También actúa como conductancia porque se concibe que las cargas fluyen a través de la membrana. Es una conductancia que se acopla a una batería porque de este fluir a través de la membrana dependerá la concentración relativa de iones dentro y fuera de la celda. Y luego, están los canales iónicos que son estras proteínas que se asientan sobre los lípidos junto al aire y que pueden permitir el flujo de iones. Pero este hecho de permitir que los iones fluyan está regulado por la forma de la proteína de modo que convebimos esos canales iónicos como conductancia que son variables y que también están acoplados a una batería, y la conductancia en realidad depende del propio potencial de membrarna.

Si vamos a la física de estos dispositivos y describimos la corriente que fluye a través de ellos, aplicaremos la ecuación de Kirchhoff. Es decir, cuando una corriente llega a un nodo tendrá que pasar por cualquiera de las diferentes ramas que salen de ese nodo. Esto significa que la corriente que incide sobre la membrana cargará el condensador ($C$) o se filtrará a través de la membrana ($g_L$). Aquí hemos usado:

- $C_m$ para la capacitancia de la membrana
- $g_L$ para la conductancia de la membrana
- $E_L$ para el potencial de equilibrio o el potencial de fuga de la membrana

Y luego está la corriente que fluye a través de los diferentes canales iónicos

---

# Leaky Integrate-and-Fire

Ahora bie, estos diferentes canales iónicos son de diferentes tipos. El canal iónico de sodio ($Na$) y el canal iónico de potasio ($K$) generan el potencial de acción. Pero también hay muchos otros canales iónicos que no participan en la generación de potenciales de acción. Entonces el enfoque de LIF es ignorar primero aquellos canales iónicos que no están involucrados en la generación del potencial de acción y reemplazar la generación de un potencial de acción, la maquinaria involucrada en hacerlo, por la fenomenología de esto. Esto es un umbral, Una vez que alcanzamos cierto umbral de voltaje, los canales $Na$ y $K$, particularmente $Na$, se activan y desencadena el potencial de acción. Lo cual, una vez realizado el potencial de acción, restablece el potencial de membrana y la dinámica continúa desarrollándose. Entonces, vamos a remplazar esas dos corrientes por un umbral externo seguido de un reinicio.

Las ecuaciones del modelo son:

- Tenemos una ecuacion diferencuial de primer órden para el potencial de membrana $V$ en función de una corriente de entrada $I$:
  $$C_m \frac{dV}{dt} = -g_L (V-E_L) + I$$
- Y tenemos una condición de umbral, cada que el potencial de membrana alcance el umbral detendremos la dinámica y reiniciaremos solo un delta de tiempo después. Este delta es el periodo refractario absoluto y corresponde al tiempo que tarda en generarse un potencial de acción, que es aproximadamente uno o dos milisegundos.
  $$\text{Si } V(t) = V_{th} \text{ entonces } V(t + \Delta) = E_L$$
  Y luego restablecemos el potencial de membrana para decir que el potencial de equilibrio pordría ser otra cosa, para finalmente seguir la misma ecuación diferencial de primer órden.

Consideraremos un aumento gradual de la corriente en algún momento $t_0$ y la corriente se mantiene constante durante ese tiempo, despues de eso se liberará. Y considerarmos una corriente que es lo suficientemente débil como para que no alcancemos el umbral del potencial de acción, entonces el potencial de membrana se verá así: permanece en el potencial de equilibrio cuando la corriente es cero y cuando llegan los pasos de corriente el potencial de membrana aumenta porque la corriente está cargando el capacitor. Pero a medida que aumenta el potencial de la membrana, fluye cada vez más corriente a través de la fuga y en algún momento, la corriente que fluye a través de la fuga compensa la corriente que fluye desde las dendritas y las sinapsis y alcanzamos un estado estable y no hay más cambios en el potencial de membrana como se observa en la figura. Y una vez que la corriente es liberada, necesitamos volver al potencial de equilibrio y seguimos la misma curva pero a la inversa. Esta curva se puede calcular resolviendo la siguiente ecuacion diferencial ordinaria, a la que llamaremos **estado actual del subumbral**

$$V(t) = (\frac{I}{g_L} + E_L)[1 - e^{\frac{-t}{\tau_m}}]$$

De esta ecuación obtenemos una relajación exponencial hasta un estado estacionario, y esta relajación exponencial seguirá un curso de tiempo que se caracteriza por la constante de tiempo de la membrana, que es simplemente la relación entren la capacitancia y la fuga $\tau_m = \frac{C_m}{g_L}$ y esto suele ser entre 10 y 50 ms en neuronas reales.

Ahora, aumentamos el paso de modo que el potencial de membrana alcance el umbral y en ese caso seguiremos la condición de reincio y la condición de umbral, de forma que detengamos la dinámica, y, decimos que estamos logrando un pico pada despues del delta del tiempo reiniciamos la dinámica en el potencial de equilibrio. Como la corriente sigue siendo alta, seguimos aumentando el potencial de membrana hasta que alcancemos nuevamente el umbral, generamos otro pico y comenzamos nuevamente. El tiempo entre picos sucesivos se llama **intervalo entre picos** y uno durante este tiempo es la **frecuencia de disparo**. Y para una frecuencia constante el intervalo entre picos permanecerá constante y solo cambiará a medida que cambie la corriente de entrada.

Pero, ¿esto es realista? ¿esto es lo que realmente hacen las neuronas?

La suposición principal aquí es que hemos asumido que los potenciales de acción siempre tienen la misma forma y no tienen un curso de tiempo variable

---

# Resumen

Los modelos LIF son una aproximación útil de la dinámica compleja de las neuronas reales.
