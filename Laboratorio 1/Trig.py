import math 
import datetime

class Trig():
    def __init__(self):
        self.valorPI = ''
        self.file = ''

    def valordePI(self):
        resultado = math.pi
        return resultado

    def sinPI(self):
        resultado = math.sin(math.pi)
        return resultado

    def cosPI(self):
        resultado = math.cos(math.pi)
        return resultado

    def tanPI(self):
        resultado = math.tan(math.pi)
        return resultado
    
    def createfile(self,name):
        try:
            file = open(name,'x')
            print('Archivo log.txt creado.')
            return file
        except FileExistsError: 
            print('Archivo log.txt ya existe, agregando datos nuevos.')
        file = open(name, 'a')
        return file 
        
    def gettime(self):
        time = datetime.datetime.now()
        return time