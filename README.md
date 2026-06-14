Comparación entre Programación Tradicional y Programación Orientada a Objetos

Autor
Dorys Jeaneth Torres Guerrero
Descripción 
Este repositorio incluye dos aplicaciones en Python diseñadas para abordar dos enfoques de programación:
 	Programación Tradicional 
 	Programación Orientada a Objetos
Ambas aplicaciones permiten gestionar y exhibir la información fundamental de las mascotas (nombre, tipo y edad
Estructura del proyecto
text
programacion_tradicional/
└── tradicional.py

programacion_poo/
├── mascota.py
└── main.py

Reflexión
La Programación tradicional organiza el código a través de funciones secuenciales que operan de manera independiente con datos externos. Los atributos de cada mascota son tratados como variables individuales en el hilo principal del programa, siendo transmitidos como parámetros a las funciones que los requieren.
Por otro lado, la Programación Basada en Objetos agrupa la solución mediante clases y objetos que combinan los datos (atributos como nombre, tipo y edad) con los comportamientos correspondientes (métodos como exhibir información o emitir un sonido) dentro de una única entidad lógica.
Durante el desarrollo, se pudo notar que la Programación Basada en Objetos mejora la organización y modularidad del código. En vez de manejar variables sueltas, permite crear múltiples objetos independientes (animal1, animal2) a partir de una sola plantilla (la clase Animal), reflejando las entidades del mundo real de manera mucho más estructurada, escalable y natural.
