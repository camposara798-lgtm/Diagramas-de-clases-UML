class Autor():
    
    #constructor
    def __init__(self, nombre, nacionalidad):
        self.__nombre=nombre
        self.__nacionalidad=nacionalidad
        
    def obtenerNombre(self):
        return self.__nombre
    def obtenerNacionalidad(self):
        return self.__nacionalidad
    
    def modificarNombre(self,nombre):
        self.__nombre=nombre
    def modificarNacionalidad(self,nacionalidad):
        self.__nacionalidad=nacionalidad
    
class Libro():
    #Constructor
    def __init__(self,titulo,genero,autor):
        self.titulo=titulo
        self.genero=genero
        self.autor=autor
        
class biblioteca():
    
    def __init__(self,nombre):
        self.nombre=nombre
        self.libro=[]
    def __init__(self,libro):
        self,libro.append(libro)
        
class usuario():
    def __init__(self,identificacion,nombre,correo):
        self.identificacion=identificacion
        self.nombre=nombre
        self.correo=correo
    def saludar(self):
        print("Hola desde usuario")

class Estudiante(usuario):
    def __init__(self,icfes,identificacion,nombre,correo):
        super().__init__(identificacion, nombre, correo)
        self.icfes=icfes
    
    def saludar(self):
        print(f"Desde usuario. Hola soy un objeto de tipo {type(self).__name__}")
    
        
class Docente(usuario):
    def __init__(self, especialidad,identifiacion,nombre,correo):
        super().__init__(self,especialidad,nombre)
        
        
class prestamo():
    
    def __init__(self,fechaPrestamo,fechaDevolucion):
        self.fechaPrestamo=fechaPrestamo
        self.fechaDevolucion=fechaDevolucion
        self.usuario=None
        self.libroPrestamo=[]
        
    def registrarPrestamo(self,libro,autor):
        self.usuario= usuario
        self.libro=libro
        
