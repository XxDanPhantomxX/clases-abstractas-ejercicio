from empleados import *
from reportes import *
from programacion import *
import datetime

empleados = [
    Gerente("Roberto", "Amezcua", Matutino()),
    Gestora("Alejandra", "Vivas", Matutino()),
    Gestora("Selene", "Ruiz", Matutino()),
    Tecnico("Artemio", "Figueroa", Vespertino()),
    Tecnico("Salvador", "Dali", Matutino()),
    Administrador("Marco", "Aurelio", Matutino()),
    Tecnico("Rolando", "Alcaraz", Matutino())]

reportes = [
    ReporteContabilidad(empleados),
    ReporteEmpleados(empleados),
    ReporteProgramacion(empleados),
    # ReporteInventario(empleados)
]

for r in reportes:
    print(r.print_reporte())

#e = Gerente("Juan", "Perez", Matutino())