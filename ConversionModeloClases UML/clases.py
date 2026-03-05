class Empresa():
    
    def __init__(self, nombre):
        self.nombre=nombre
        self.departamentos=[]
    def agregar_departamento(self,departamento):
        self.departamentos.append(departamento)
    def mostrar_departamento(self):
        for d in self.departamentos:
            print(d.nombre)

class Departamento():
    def __init__(self,nombre):
        self.nombre=nombre
        self.empleados=[]
    def agregar_empleado(self,empleado):
        self.empleados.append(empleado)
    def mostrar_empleado(self):
        for e in self.empleados:
            print(e.get_nombre())
class Contrato():
    def __init__(self,tipo,salario):
        self.tipo=tipo
        self.salario=salario
    def mostrar_contrato(self):
        print("Tipo:",self.tipo)
        print("Salario:",self.salario)

class Empleado():
    def __init__(self,nombre,edad):
        self.__nombre=nombre
        self.__edad=edad
        self.contrato=None
    #Encapsulamiento
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nombre):
        self.__nombre=nombre
    def get_edad(self):
        return self.__edad
    def set_edad(self,edad):
        self.__edad=edad
    def asignar_contrato(self,contrato):
        self.contrato=contrato 
    def mostrar_info(self):
        print("Empleado:",self.__nombre)
        print("Edad:",self.__edad)

    #Polimorfismo
    def trabajar(self):
        print("El empleado esta trabajando")

class Administrativo(Empleado):
    def trabajar(self):
        print("El administrativo gestion documentos")

class Operativo(Empleado):
    def trabajar(self):
        print("El operativo realiza tareas tecnicas")


        