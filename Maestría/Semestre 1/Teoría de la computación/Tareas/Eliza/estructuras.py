'''
    estructuras_generales: es el diccionario principal. Cada elemento de la lista es un elemeto doble;
        el primero es una expresion regular, y el segundo es una lista de posibles respuestas con grupos 
        de macros etiquetados como %1, %2, etc.
'''
estructuras_generales = [

    [r'Que puedes hacer por mi\??',
        ['''Puedo hacer las siguientes cosas:
        - Platicar contigo
        - Hacer busquedas en internet
        - Decirte datos curiosos
        - Responderte preguntas acerca de programación orientada a objetos (OOPS)''']],

    [r'Como busco algo\??',
        ['''Intenta escribiendo lo siguiente:
        
        Busca Google''']],

    [r'(.*) OOPS\??',
        ['''Bueno, las siglas OOPS definen el Sistema de Programación Orientada a Objetos (Object Oriented Programming system), con el cual los programas pasan a ser considerados una colección de objetos. Cada uno de estos objetos es una parte de una clase.''']],

    [r'(.*) conceptos basicos de OOPS\??',
        ['''Tenemos 4, y son:
        Encapsulación
        Herencia
        Polimorfismo
        Abstracción.''']],

    [r'(.*) clase\??',
        ['''Muy sencillo, una clase es la representación de un cierto tipo de objeto. Es el plan que define las características de un objeto.''']],

    [r'(.*) objeto\??',
        ['''Un objeto es parte de una clase. Tiene su propio estado, comportamiento y definición.''']],
        
    [r'(.*) polimorfismo\??',
        ['''El polimorfismo es la asignación de un valor que se da a una subclase, o que se había declarado ya en la clase principal.''']],

    [r'(.*) encapsulacion\??',
        ['''La encapsulación es una característica del objeto y guarda todos los datos ocultos. Estos datos (ocultos) pueden estar limitados para los que forman esa clase. Sus niveles son, internos, protegidos, públicos,  protegidos internos, y privados''']],

    [r'(.*) herencia\??',
        ['''La herencia es el concepto con el cual se aclara que una clase divide la estructura y comportamiento definidos en otra clase. Si la herencia es aplicada a una clase se le llama herencia única, pero si la herencia depende de diferentes clases,  se le conoce como múltiple.''']],

    [r'(.*) manipuladores\??',
        ['''Se denomina manipuladores a las funciones que se utilizan junto con operadores de inserción (<<) y extracción (>>) en un objeto. Se pueden identificar como ejemplos: endl y setw.''']],

    [r'Como se define un constructor\??',
        ['''Se define así al método que se utiliza para iniciar el estado de un objeto, y está incluido desde el momento que se crea el objeto. El constructor tiene unas  reglas que son:

        El constructor tiene un nombre, que debe ser el mismo nombre de la clase.
        El constructor no puede tener ningún tipo de retorno.''']],

    [r'Como se define un destructor\??',
        ['''El destructor es el método que se nombra de forma automática cuando el objeto está realizado de alcance o destruido. El destructor debe llevar  el mismo nombre de la clase, pero lleva el símbolo de tilde está colocado antes del nombre.''']],

    [r'(.*) funcion en linea\??',
        ['''La función en línea o inline es la técnica usada por  compiladores y que  indica que introduzcas el cuerpo entero de la función, siempre que la función se use  el código que es fuente del programa.''']],

    [r'(.*) funcion virtual\??',
        ['''La función virtual es una función parte de una clase y su función puede ser eliminada en su clase derivada. Esta función se puede implementar usando una palabra clave que se denomina virtual, y se puede presentar durante la declaración de la función. Un ejemplo de función virtual, puede ser un token en C ++, el cual se puede lograr en lenguaje C, a través del uso de punteros de función (function pointers).''']],

    [r'(.*) friend function\??',
        ['Esta función es el ‘amigo’ de una clase a la que se le deja entrar  a datos públicos, protegidos o  privados, en esa misma clase.  Los amigos de clase se pueden verse afectados por la palabra clave de control de entrada como, público, privado o protegido.']],
    
    [r'(.*) sobrecarga de funciones\??',
        ['''La función de sobrecarga es una funcion normal, pero puede realizar varias tareas.  Asimismo, permite crear varios métodos con un mismo nombre que solo los va a distinguir el tipo de entrada y salida que tiene la función.
        Ejemplo:
        
        void add(int&amp; a, int&amp; b);
        void add(double&amp; a, double&amp; b);
        void add(struct bob&amp; a, struct bob&amp; b);
        ''']],

    [r'(.*) sobrecarga del operador\??',
        ['Es una función donde se aplican varios operadores y que depende de los argumentos. Operator,-,* puede ser usado para pasar a traves de la funcion y tiene su propia prioridad para ejecutar.']],

    [r'(.*) clase abstracta\??',
        ['Una clase abstracta es aquella clase que no puede ser instanciada. No se puede crear un objeto usando una clase abstracta pero puede ser heredado. Una clase abstracta solo puede contener el método abstracto. Por esta razón, Java permite solamente el método abstracto en la clase abstracta, sin embargo, para otros lenguajes sólo permite el método no abstracto.']],

    [r'(.*) operador ternario\??',
        ['El operador ternario es el que toma tres argumentos, también se llama un operador condicional y toma resultados y argumentos. Los argumentos y los resultados son de diferentes tipos de datos, y dependen de la función.']],

    [r'(.*) metodo de finalizacion\??',
        ['Este método ayuda a hacer operaciones de limpieza en  recursos que no son utilizados  en la actualidad. El método de finalización está protegido y solo se puede acceder por medio de esta clase o una derivada.']],

    [r'(.*) diferentes tipos de argumentos\??',
        ['''Hay dos tipos de argumentos:

        Llamada por valor (call by value): el valor que se haya pasado se modifica solo dentro de la función, y reitera el mismo valor que sea el cual se va a pasar  a la función.
        Llamada por referencia (call by reference): el valor pasado cambia tanto dentro como fuera de la función y arroja el mismo valor o distinto.''']],

    [r'(.*) palabra super clave\??',
        ['La palabra clave super es la que se utiliza para llamar el método overridden, el cual anula uno de sus métodos de superclase. La palabra clave deja entrar a métodos sobrescritos y a miembros escondidos de la superclase. Asimismo, reenvía una llamada de un constructor a otro constructor.']],

    [r'(.*) metodo de anulacion\??',
        ['Se conoce como método de anulación u overriding a una característica que deja que una subclase suministre la implementación de un método que anula en la clase principal. Se realiza la anulación de la implementación en la superclase al dar el mismo nombre de método, parámetro y tipo de retorno.']],

    [r'(.*) interfaz\??',
        ['La interfaz es la colección que tiene el método abstracto. Cuando la clase implementa una herencia, de la misma manera hereda los métodos abstractos que tiene una interfaz.']],

    [r'(.*) manejo de excepciones\??',
        ['La excepción es aquel evento que se suscita cuando se está ejecutando un programa. Las excepciones pueden ser de varios tipos: de tiempo, ejecución de error. Esas excepciones se llevan, por medio de un mecanismo de manejo de excepciones como son palabras clave try, catch y throw.']],

    [r'(.*) tokens\??',
        ['El token es reconocido por un compilador y no puede ser divido en elementos-componentes. Entre los tokens podemos ubicar: la palabras clave, los identificadores, los constantes, los literales de string y los operadores. Sin embargo, también son considerados tokens, las comas, paréntesis, llaves y corchetes.']],

    [r'(.*) diferencia (.*) entre overloading y overriding\??',
        ['Overloading es un enlace estático, y  la overriding es un enlace dinámico. Overloading es el mismo método con distintos argumentos, y puede devolver o no, el mismo valor en la misma clase. En cambio, overriding es el mismo nombre del método, y con los mismos argumentos y tipos de devolución asociados a la clase y a su clase secundaria.']],

    [r'(.*) diferencia (.*) entre clase y objeto\??',
        ['El objeto es una instancia de una clase. Los objetos tienen información múltiple,  las clases no guardan ningún tipo de información. La definición de propiedades y funciones se realiza en clase y puede utilizarla el objeto. La clase posee subclases, pero el objeto no posee subobjetos.']],

    [r'(.*) abstraccion\??',
        ['La abstracción es una de la característica de OOPS que muestra solamente los detalles y que necesita el cliente de un objeto. Ejemplo: Al encender el televisor no se necesita ver todas sus funciones, lo que sea que se requiera para encender la TV se puede hacer usando una clase abstracta.']],

    [r'(.*) modificadores de acceso\??',
        ['''Los modificadores de acceso son aquellos que determinan el alcance que tiene el  método o las variables a las cuales se entra a través de otros objetos o clases. Hay 5 tipos de modificadores de acceso:

        Private
        Protected
        Public
        Friend
        Protected Friend''']],

    [r'(.*) modificadores sellados\??',
        ['Los modificadores sellados (sealed modifiers) son los modificadores de acceso a los cuales no se les permiten ser heredados por los métodos. Estos también se pueden aplicar a eventos, propiedades y métodos. Es un modificador que no se puede aplicar a miembros estáticos.']],

    [r'(.*) diferencia (.*) entre between new y override\??',
        ['El modificador ‘new’ le va a indicar al compilador que utilice la nueva implementación y no la función de clase base. En cambio,  el modificador override permite anular la función de clase base.']],

    [r'(.*) tipos de constructores\??',
        ['''Los  constructores, son de tres tipos:

        El constructor por defecto / sin parámetros.
        El constructor paramétrico / con parámetros: Este constructor pasa argumentos en forma simultánea y puede crear una nueva instancia de una clase
        El constructor copy: este constructor puede crear un nuevo objeto como una copia de un objeto que ya existe.''']],

    [r'(.*) early\??',
        ['La vinculación temprana es la asignación de valores a variables durante el tiempo de diseño']],

    [r'(.*) late binding\??',
        ['La vinculación tardía es la asignación de valores a las variables en el tiempo de ejecución.']],

    [r'(.*) puntero this\??',
        ['El puntero (pointer) ‘this’ define al objeto actual de una clase. Esta palabra clave es utilizada como puntero que va a distinguir entre el objeto actual y el objeto global. Es decir, está referido al objeto actual.']],

    [r'(.*) diferencia (.*) entre estructura y clase\??',
        ['El  acceso a la clase es privado, pero el acceso predeterminado de la estructura es público. La estructura se usa para reunir datos pero la clase puede ser utilizada para reunir datos y a su vez  métodos. Las estructuras son exclusivas para datos, no requieren validación estricta. En cambio, las clases se utilizan para encapsular y heredar datos, por lo que requieren validación estricta.']],

    [r'Platiquemos',
        ["Claro, ¿de qué quieres platicar?"]],

    [r'Que eres',
        ['''Soy un chatbot totalmente en español basado en Eliza.
        Si quieres saber que es Eliza, pregúntame "que es Eliza"''']],

    [r'Que es Eliza',
        ['''Eliza es un programa informático diseñado en el MIT entre 1964 y 1966 por Joseph Weizenbaum. 
        Eliza fue uno de los primeros programas en procesar lenguaje natural. 
        El mismo parodiaba al psicólogo Carl Rogers e intentaba mantener una conversación de texto coherente con el usuario.
        Fuente: Wikipedia''']],

    [r'(.*) dato curioso',
        ['''En 1998, Sony tuvo la oportunidad de comprar los derechos de casi todos los personajes de Marvel por 25 millones de dólares. Optaron por no hacerlo, salvo por Spider-Man, que compraron por 7 millones. ¿El motivo? No consideraban que el resto de personajes de Marvel fuesen ‘relevantes’''',
        '''Los nazis quemaron todos los libros de Sigmund Freud. Cuando se enteró, el conocido psicólogo “alabó” el progreso: “En la Edad Media me habrían quemado a mi. Ahora están contentos con quemar mis libros”''',
        '''En 1959, una bibliotecaria de Carolina del Sur llamó a la Policía porque un niño negro de 9 años no quería marcharse. 
        El niño obtuvo después un doctorado en Física por el MIT y murió en 1986, como uno de los astronautas a bordo del transbordador espacial Challenger. 
        La biblioteca que en el pasado no le dejaba coger libros ostenta ahora su nombre, Ronald McNair''',
        '''Angelina Jolie intentó contratar a un sicario para que le matase cuando era joven, porque creía que para su familia un asesinato sería algo más fácil de sobrellevar que un suicidio. 
        El sicario en cuestión terminó por hablar con ella y consiguió convencerla para que esperara un mes y poder buscar tratamiento para su depresión''',
        '''En 1880, el director del Observatorio Astronómico de Harvard estaba tan frustrado con su equipo que a menudo decía “¡Mi sirvienta escocesa lo haría mil veces mejor!”. 
        Y lo hizo. El director contrató a su sirvienta, Williamina Fleming, que se convirtió en directora de equipo durante décadas, clasificó decenas de estrellas y descubrió la nebulosa Cabeza de Caballo en la Constelación de Orión''',
        '''El cantante Billy Joel nunca vende los asientos de primera fila para ver a sus verdaderos fans delante de él. Suele dárselos a gente que tiene entradas baratas, para demostrar que no siempre la primera fila es para la gente rica''',
        '''Carrie Fisher le envió un paquete que contenía una lengua de vaca a un productor que había abusado de una amiga suya. La actriz envió una nota junto al paquete que decía: “La próxima cosa que envíe será algo tuyo en una caja mucho más pequeña”''']],

    [r'No lo sabia',
        ["Todos los días aprendemos algo nuevo",
        "Lo sé, yo también me impresioné cuando lo supe"]],

    [r'(.*) como estas\?',
        ["Desafortunadamente soy una máquina y no puedo sentir",
        "Si fuera humano, supongo que estaría bien",
        "Eso es una buena pregunta, no lo sé"]],

    [r'Yo necesito (.*)',
        ["¿Por que necesitas %1?",
         "¿Realmente te ayudaria en algo conseguir %1?",
         "¿Estas seguro que necesitas %1?"]],

    [r'¿Por que no tu ([^\?]*)\??',
        ["¿En verdad crees que no %1?",
         "Tal vez con tiempo haga %1.",
         "¿En verdad quieres que %1?"]],

    [r'¿Por que no puedo ([^\?]*)\??',
        ["¿En verdad piensas que deberia poder %1?",
         "¿Si pudieras %1, que harias?",
         "¿No lo se, por que no %1?",
         "¿En verdad lo has intentado?"]],

    [r'No puedo (.*)',
        ["¿Como sabes que no puedes %1?",
         "Tal vez tu puedes %1 si trataras de hacerlo.",
         "¿Que necesitarias para que %1?"]],

    [r'Yo soy (.*)',
        ["¿Viniste conmigo porque tu eres %1?",
         "¿Por cuanto tiempo has sido %1?",
         "¿Como te sientes respecto a ser %1?"]],

    [r'Soy (.*)',
        ["¿Como te hace sentir ser %1?",
         "¿Disfrutas ser %1?",
         "¿Por que me dices que eres %1?",
         "¿Por que crees que eres %1?"]],

    [r'Tu eres ([^\?]*)\??',
        ["¿Por qué importa si soy %1?",
         "¿Preferirías que no fuera %1?",
         "Tal vez tu piensas que soy %1.",
         "Puede que sea %1... ¿Tu que crees?"]],

    [r'Que (.*)',
        ["¿Por que preguntas?",
         "¿Cómo le ayudaría una respuesta a eso?",
         "¿Que piensas?"]],

    [r'Como (.*)',
        ["¿Como supones eso?",
         "Tal vez tu puedas responder tu propia pregunta",
         "¿Que es lo que realmente estas prenguntando?"]],

    [r'Porque (.*)',
        ["¿Es esa la verdadera razón?",
         "¿Qué otras razones se te ocurren?",
         "¿Esa razón se aplica a algo más?",
         "Si %1, ¿qué otra cosa debe ser cierta?"]],

    [r'(.*) lo siento (.*)',
        ["Hay muchas veces en las que no es necesario pedir disculpas",
         "¿Qué sentimientos tienes cuando te disculpas?"]],

    [r'Hola(.*)',
        ["Hola!",
         "Hola!, ¿cómo estás?",
         "Hola, ¿cómo te encuentras hoy?"]],

    [r'Creo que (.*)',
        ["¿Dudas de %1?",
         "¿Realmente lo crees?",
         "¿Pero no estás seguro %1?"]],

    [r'(.*) amigo (.*)',
        ["Cuéntame más sobre tus amigos",
         "Cuando piensas en un amigo, ¿qué te viene a la mente?",
         "¿Por qué no me hablas de un amigo de la infancia?"]],

    [r'Si',
        ["Pareces muy seguro",
        "¿Si?"
         "De acuerdo, pero ¿puedes explicarte un poco más?"]],

    [r'(.*) ordenador(.*)',
        ["¿Realmente estás hablando de mí?",
         "¿Te parece extraño hablar con un ordenador?",
         "¿Cómo te hacen sentir los ordenadores?",
         "¿Te sientes amenazado por los ordenadores?"]],

    [r'Es (.*)',
        ["¿Crees que es %1?",
         "Tal vez sea %1... ¿qué crees?",
         "Si fuera %1, ¿qué harías?",
         "Bien podría ser ese %1"]],

    [r'Es (.*)',
        ["Pareces muy seguro",
         "Si te dijera que probablemente no es %1, ¿qué sentirías?"]],

    [r'Puedes ser ([^\?]*)\??',
        ["¿Qué te hace pensar que no puedo %1?",
         "Si pudiera %1, ¿entonces qué?",
         "¿Por qué preguntas si puedo %1?"]],

    [r'Puedo ser ([^\?]*)\??',
        ["Quizás no quieras %1",
         "¿Quieres poder %1?",
         "Si pudieras %1, ¿lo harías?"]],

    [r'Eres (.*)',
        ["¿Por qué crees que soy %1?",
         "¿Te complace pensar que soy %1?",
         "Quizás te gustaría que fuera %1",
         "¿Quizás estás hablando realmente de ti mismo?"]],

    [r'Tu eres (.*)',
        ["¿Por qué dices que soy %1?",
         "¿Por qué crees que soy %1?",
         "¿Estamos hablando de ti o de mí?"]],

    [r'No puedo (.*)',
        ["¿No eres realmente %1?",
         "¿Por qué no %1?",
         "¿Quieres %1?"]],

    [r'Me siento (.*)',
        ["Bien, cuéntame más sobre estos sentimientos",
         "¿Sueles sentir %1?",
         "¿Cuándo sueles sentir %1?",
         "Cuando sientes %1, ¿qué haces?"]],

    [r'Tengo (.*)',
        ["¿Por qué me dices que tienes %1?",
         "¿Realmente tienes %1?",
         "Ahora que tienes %1, ¿qué vas a hacer ahora?"]],

    [r'Yo haría (.*)',
        ["¿Podrías explicar por qué harías %1?",
         "¿Por qué harías %1?",
         "¿Quién más sabe que harías %1?"]],

    [r'Hay (.*)',
        ["¿Crees que hay %1?",
         "Es probable que haya %1",
         "¿Le gustaría que hubiera %1?"]],

    [r'Mi (.*)',
        ["Ya veo, tu %1.",
         "¿Por qué dices que tu %1?",
         "Cuando tu %1, ¿cómo te sientes?"]],

    [r'Tú (.*)',
        ["Deberíamos estar discutiendo sobre ti, no sobre mí",
         "¿Por qué dices eso de mí?",
         "¿Por qué te importa si yo %1?"]],

    [r'Por qué (.*)',
        ["¿Por qué no me dices la razón de %1?",
         "¿Por qué crees que %1?"]],

    [r'Quiero (.*)',
        ["¿Qué significaría para ti si obtuvieras %1?",
         "¿Por qué quieres %1?",
         "¿Qué harías si obtuvieras %1?",
         "Si tienes %1, ¿qué harías?"]],

    [r'(.*) madre(.*)',
        ["Cuéntame más sobre tu madre",
         "¿Cómo era tu relación con tu madre?",
         "¿Qué sientes por tu madre?",
         "¿Cómo se relaciona esto con tus sentimientos de hoy?",
         "Las buenas relaciones familiares son importantes"]],

    [r'(.*) padre(.*)',
        ["Cuéntame más sobre tu padre",
         "¿Cómo te hizo sentir tu padre?",
         "¿Qué sientes por tu padre?",
         "¿La relación con tu padre se relaciona con tus sentimientos de hoy?",
         "¿Tienes problemas para mostrar afecto con tu familia?"]],

    [r'(.*) niño(.*)',
        ["¿Tenías amigos íntimos cuando eras niño?",
         "¿Cuál es tu recuerdo favorito de la infancia?",
         "¿Recuerdas algún sueño o pesadilla de la infancia?",
         "¿Se burlaban a veces de ti los otros niños?",
         "¿Cómo crees que tus experiencias de la infancia se relacionan con tus sentimientos actuales?"]],

    [r'(.*)\?',
        ["¿Por qué lo preguntas?",
         "Por favor, considera si puedes responder a tu propia pregunta",
         "¿Tal vez la respuesta esté dentro de ti mismo?",
         "¿Por qué no me lo dices?"]],

    [r'salir',
        ["Adiós. Si necesitas algo más, no dudes en volver",
         "Hasta la próxima :)",
         "Serán 150 pesos, pague al cerrar. Gracias por utilizar Eliza."]],

    [r'Bien',
        ["Me alegro que te encuentres bien",
        "Excelente!"]],

    [r'Mal',
        ["¿Por qué estás mal?",
        "¿Pasó algo?",
        "Platícame porque te sientes así"]],

    [r'(.*)',
        ["Por favor, cuéntame más.",
         "Cambiemos un poco el enfoque... Háblame de tu familia",
         "¿Puedes explicarlo mejor?",
         "¿Por qué dices que %1?",
         "Ya veo",
         "Muy interesante",
         "%1?",
         "Ya veo.  ¿Y qué te dice eso?",
         "¿Cómo te hace sentir?",
         "¿Cómo te sientes cuando dices eso?"]]
]