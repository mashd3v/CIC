;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Tarea 4.1: Programación Funcional
; Teoría de la computación
; Miguel Angel Soto Hernandez
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


; Función cero
(defun cero() 
    (return-from cero 0))
(format t "Función cero = ~d ~%" (cero))


; Función sigma
(defun sigma(x)
    (return-from sigma (+ x 1)))
(format t "Función sigma de 3 = ~d ~%" (sigma 3))


; Función proyeccion
(defun proyeccion(m lista)
    (nth m lista))
(format t "Función de proyección 2 para la lista (2 4 6) = ~d ~%"(proyeccion 2 (list 2 4 6)))


; Función suma
(defun suma(x y)
    (if (= y 0)
        (progn
            (return-from suma (proyeccion 0 (list x y)))
        )
        (return-from suma (sigma(proyeccion 2 (list x y (suma x (- y 1))))))))
(format t "Función suma de 100 + 50 = ~d ~%"(suma 100 50))


; Función multiplicacion
(defun multiplicacion(x y)
    (if (or (= y 0) (= x 0))
        (progn
            (return-from multiplicacion (cero))
        )
        (return-from multiplicacion (suma x (multiplicacion x (- y 1))))))
(format t "Función multiplicación de 10 por 10 = ~d ~%"(multiplicacion 10 10))


; Función exponencial
(defun exponencial(x y)
    (if (= y 0)
        (progn
            (return-from exponencial 1)
        )
        (return-from exponencial (multiplicacion x (exponencial x (- y 1))))))
(format t "Función exponencial de 3 a la quinta = ~d ~%"(exponencial 3 5))


; Función predecesor
(defun predecesor(y)
    (if (= y 0)
        (progn 
            (return-from predecesor(cero))
        )
        (return-from predecesor(proyeccion 0 (list (- y 1) (predecesor(- y 1)))))))
(format t "Función predecesor de 100 = ~d ~%"(predecesor 100))


; Función monus (resta)
(defun monus(x y)
    (if (= y 0)
        (progn
            (return-from monus(proyeccion 0 (list x)))          
        )
        (return-from monus(predecesor(monus x (- y 1))))))
(format t "Función monus o resta de 21 - 16 = ~d ~%"(monus 21 16))


; Función igual
; Retorna un 1 si es igual o un 0 si no son iguales
(defun igual(x y)
    (return-from igual(monus 1 (suma (monus y x) (monus x y)))))
(format t "Función igual de 10 igual a 10 = ~d ~%"(igual 10 10))


; Función cociente
(defun cociente(x y)
    (if (= x 0)
        (progn
            (return-from cociente(cero))
        )
        (return-from cociente(suma (cociente (- x 1) y) (igual x (suma (multiplicacion (cociente (- x 1) y) y) y))))))
(format t "Función cociente de 10 entre 4 = ~d ~%"(cociente 10 4))


; Función ackerman
(defun ackerman(x y)
    (cond ((and (= x 0) (> y 0))
           (return-from ackerman(+ y 1)))
           ((and (> x 0) (= y 0))
           (return-from ackerman(ackerman (- x 1) 1)))
           (t(return-from ackerman(ackerman (- x 1) (ackerman x (- y 1)))))))
(format t "Función Ackerman de (3, 1) = ~d ~%"(ackerman 3 1))


; Función factorial
(defun factorial(x)
    (if (or (= x 0) (= x 1))
        (progn
            (return-from factorial 1)
        )
        (return-from factorial(multiplicacion x (factorial (predecesor x))))))
(format t "Función factorial de 6 = ~d ~%"(factorial 6))


; Función fibonacci
(defun fibonacci(x)
    (if (< x 2)
        (progn
            (return-from fibonacci x)
        )
        (return-from fibonacci(suma (fibonacci (- x 1)) (fibonacci (- x 2))))))
(format t "Función fibonacci de 5 = ~d ~%"(fibonacci 5))