import datetime

class Programacion: 
    def get_programacion_info(self):
        return f'{self.hora_entrada:%H:%M}-{self.hora_salida:%H:%M}'

class Matutino(Programacion):
    hora_entrada = datetime.time(8,00)
    hora_salida = datetime.time(16,00)
    
class Vespertino(Programacion):
    hora_entrada = datetime.time(12,00)
    hora_salida = datetime.time(20,00)