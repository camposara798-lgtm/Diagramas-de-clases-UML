from clases import *
from datetime import datetime as dt, timedelta

miBlioteca = biblioteca("sena-CTPI")

autor1 = Autor("Gabriel Garcia Marquez","Colombiano")
autor2 = Autor("Jose Eustacio Rivera","Colombiano")

libro1 = Libro("Cien Años de Soleda", "Novela",autor1)

print(f"Libro: {libro1.titulo}")
print(f"Autor: {libro1.autor.obtenerNombre()} {libro1.autor.obtenerNacionalidad()}")
print(f"Nacionalidad autor")
miBlioteca.registrarLibro(libro1)

autor3 = Autor("Robert Greene", "Estadounidense")
libro2 = Libro("Las cuarentayocho leyes del poder" , "Economia", Autor)


miBlioteca.registrarLibro(libro2)

print("Lista de libros de la biblioteca")
for libro in miBlioteca.libros:
    print(f"Titulo Libro: {libro.titulo}")
    print(f"Autor: {libro.autor.nombre}")
    print("*"*20)
    
    
Docente1 = Docente("Software",11,"Pablo Rojas","projas@sena.edu.co")
Estudiante1 = Estudiante(290,12,"Juan Lozano","jlozano@gmail.com")

fechaprestamo =dt.now #fecha actual 
print(fechaprestamo)

dias_prestamo = timedelta(days=5)
fechaDevolucion = fechaprestamo + dias_prestamo
print(fechaDevolucion)
prestamo1 = prestamo(fechaprestamo,fechaDevolucion)
prestamo1.registrarPrestamo(libro1,Estudiante1)

#autor1.nacionalidad="Mexicano"
autor1.modificarNacionalidad
print(f"Nombre Autor: {autor1.obtenerNombre()}")
print(f"Nacionalidad Autor: {autor1.obtenerNacionalidad()}")

Docente1.saludar()
Estudiante1.saludar()