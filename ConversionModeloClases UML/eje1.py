from clases import*

empresa = Empresa("Tech Solutions")

dep1 = Departamento("Sistemas")
dep2 = Departamento("Recursos Humanos")

empresa.agregar_departamento(dep1)
empresa.agregar_departamento(dep2)

emp1 = Administrativo("Mariana",30)
emp2 = Operativo("Carlos",25)

contrato1 = Contrato("Indefinido",2500)
contrato2 = Contrato("Temporal",1800)

emp1.asignar_contrato(contrato1)
emp2.asignar_contrato(contrato2)

dep1.agregar_empleado(emp1)
dep1.agregar_empleado(emp2)

empresa.mostrar_departamento()

dep1.mostrar_empleado()

emp1.mostrar_info()
emp1.trabajar()

emp2.mostrar_info()
emp2.trabajar()