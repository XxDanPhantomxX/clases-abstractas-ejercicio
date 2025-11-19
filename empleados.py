from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre, apellido, programacion):
        self._nombre = nombre
        self._apellido = apellido
        self.programacion = programacion
    
    def get_nombre_completo(self):
        return f'{self._nombre} {self._apellido}'
    
    # Obligar a las subclases a implementar el método puesto
    @property
    @abstractmethod
    def puesto(self) -> str:
        raise NotImplementedError

class Tecnico(Empleado):
    def __init__(self, nombre, apellido, programacion):
        # Envia los parámetros al constructor de la clase base
        super().__init__(nombre, apellido, programacion)
        
    @property
    def puesto(self) -> str:
        return "Técnico"
    
    salario = "$9500"
    
class Gestora(Empleado):
    def __init__(self, nombre, apellido, programacion):
        super().__init__(nombre, apellido, programacion)
        
    @property
    def puesto(self) -> str:
        return "Gestora de Cobranza"
    
    salario = "$8000"
    
class Gerente(Empleado):
    def __init__(self, nombre, apellido, programacion):
        super().__init__(nombre, apellido, programacion)
        
    @property
    def puesto(self) -> str:
        return "Gerente General"
    
    salario = "$20000"
    
class Administrador(Empleado):
    def __init__(self, nombre, apellido, programacion):
        super().__init__(nombre, apellido, programacion)
        
    @property
    def puesto(self) -> str:
        return "Administrador de Servicios de Cable"
    
    salario = "$15000"
