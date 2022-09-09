from datetime import date

class Data():
    def __init__(self, dia=0, mes=0, ano=0):
        self.dia = dia 
        self.mes = mes 
        self.ano = ano 
        
    @property
    def dia(self):
        return self.__dia 
    
    @dia.setter
    def dia (self, dia):
        self.__dia = dia
    
    @property
    def mes(self):
        return self.__mes
    
    @mes.setter
    def mes (self, mes):
        self.__mes = mes 
        
    @property
    def ano(self):
        return self.__ano 
    
    @ano.setter
    def ano (self, ano):
        self.__ano = ano 
        
    def atual_data(self):
        return date.today()
        
    
    def __str__(self):
        if self.dia == 0 or self.mes == 0 or self.ano == 0:
            pass 
        else:
            return f'{self.dia}/{self.mes}/{self.ano}'
    
    