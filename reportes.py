import datetime
from abc import ABC, abstractmethod

class Reporte (ABC):
    def __init__(self, lista_empleados):
        self._lista_empleados = lista_empleados
    
    @property
    @abstractmethod
    def print_reporte(self):
        raise NotImplementedError

class ReporteContabilidad(Reporte):
    def __init__(self, lista_empleados):
        super().__init__(lista_empleados)
    
    class Encabezado:
        """ Clase Privada para ReporteContabilidad"""
        
        def __init__(self) -> None:
            #Lógica para el encabezado
            self.fecha = datetime.date.today()
        
        def imprimir_encabezado(self):
            print("="*45)
            print(f" FINANZAS Y CONTABILIDAD | Fecha: {self.fecha}")
            print("="*45)
            print(f"{'Empleado':<24} | {'Salario':>10}")
            print("-"*45)
    
    def print_reporte(self):
        encabezado = self.Encabezado()
        encabezado.imprimir_encabezado()
        # print("************* REPORTE DE CONTABILIDAD ****************")
        for e in self._lista_empleados:
            print(f'{e.get_nombre_completo()}, {e.salario}')
        
        print("="*45 + "\n")
        
class ReporteEmpleados(Reporte):
    def __init__(self, lista_empleados):
        super().__init__(lista_empleados)
    
    def print_reporte(self):
        print("************* REPORTE DE EMPLEADOS ****************")
        for e in self._lista_empleados: 
            print(f'{e.get_nombre_completo()}, {e.puesto}')  

class ReporteProgramacion(Reporte):
    def __init__(self, lista_empleados):
        super().__init__(lista_empleados)
    
    def print_reporte(self):
        print("************* REPORTE DE PROGRAMACION ****************")
        for e in self._lista_empleados: 
            print(f'{e.get_nombre_completo()}, {e.programacion.get_programacion_info()}')

class ReporteInventario(Reporte):
    pass