class Empleado:
    def __init__(self, nombre, apellido, programacion):
        self._nombre = nombre 
        self._apellido = apellido
        self.programacion = programacion
    
    def get_nombre_completo(self):
        return f'{self._nombre} {self._apellido}'

class Tecnico(Empleado):
    puesto = "Técnico"
    salario = "$9500"

class Gestora(Empleado):
    puesto = "Gestora de Cobranza"
    salario =  "$8000"

class Gerente(Empleado):
    puesto = "Gerente General"
    salario = "$20000"

class Administrador(Empleado):
    puesto = "Administrador de Servicios de Cable"
    salario = "$15000"