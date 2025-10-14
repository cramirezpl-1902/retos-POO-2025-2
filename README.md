# retos-POO-2025-2
Bienvenido este repositorio es creado con el fin de subir los retos del semestre de la materia POO (programacion orientada objetos), en la Universidad Nacional de Colombia en el segundo semestre del año 2025.
## ¿ En que consiste el reto 1 ?
En el reto 1 nos piden desarrollar una serie de ejercicios prácticos en Python, cada uno como un programa independiente. Los ejercicios incluyen operaciones matemáticas básicas entre dos números, verificación de palíndromos sin usar slicing, filtrado de números primos desde una lista, cálculo de la mayor suma entre elementos consecutivos, y detección de palabras que comparten los mismos caracteres. La idea es aplicar funciones, condicionales y lógica básica para resolver cada problema.
## ¿cuales eran los ejercicios del reto 1 ?
1.Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3).
2.Realice una función que permita validar si una palabra es un palíndromo. Condición: No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.
3.Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.
4.Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.
5.Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres. e.g. entrada: ["amor", "roma", "perro"], salida ["amor", "roma"].
La solucion a cada ejercicio se podra encontrar en cada archivo que lleve el nombre del ejercicio correspondiente.
# RETO 2
## ¿ en que consiste el reto 2?
Problema PLanteado:
Elija un problema de la vida real (sistema de gestión de biblioteca, negocio de compra-venta, automóvil, etc) que se pueda modelar a través de objetos y clases. Plantee las relaciones de clases, composiciones, propiedades y comportamientos del sistema en uno mas diagramas tipo UML.
## Solucion 
Un sistema UML de compra y venta de videojuegos.
<img width="751" height="731" alt="reto 2 drawio" src="https://github.com/user-attachments/assets/53b889a8-cbf0-42af-b265-2b7dd63cf5b2" />

# RETO 3
1.Escenario de restaurante: desea diseñar un programa para calcular la factura del pedido de un cliente en un restaurante.

-Definir una clase base MenuItem: Esta clase debe tener atributos como nombre, precio y un método para calcular el precio total.

-Cree subclases para diferentes tipos de elementos de menú: herede de MenuItem y defina propiedades específicas para cada tipo (por ejemplo, Bebida, Aperitivo, Plato principal).

-Definir una clase Order: Esta clase debe tener una lista de objetos MenuItem y métodos para agregar artículos, calcular el monto total de la factura y potencialmente aplicar descuentos específicos según la composición del pedido.

Cree un diagrama de clases con todas las clases y sus relaciones. El menú debe tener al menos 10 elementos. El código debe seguir las reglas PEP8.

# RETO 4 
entrega del reto 4 del curso de poo.
## RESTAURANTE RETO 4
Agrega setters y getters a todas las subclases de los elementos del menú.

Sobrescribe el método calcular_precio_total() (o calculate_total_price()) de acuerdo con la composición del pedido (por ejemplo, si el pedido incluye un plato principal, aplica algún descuento en las bebidas).

Agrega la clase Pago() (Payment()) siguiendo el ejemplo de clase proporcionado.
Cristian David Ramirez Plazas.
T:i : 1014668499.
