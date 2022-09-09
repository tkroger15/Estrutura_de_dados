class Aluno():
    def __init__(self, nome, matricula):
        self.matricula = matricula 
        self.nome = nome
        self.__notas = []
        
    @property
    def nome(self):
        return self.__nome 
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome            
    
    @property
    def matricula(self):
        return self.__matricula 
    
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula
        
    def adicionar_nota(self, nota):
        if nota > 10 or nota < 0:
            print('Insira uma nota válida: entre 0 a 10')
        else:
            self.__notas.append(nota)
        
    def media(self):
        if len(self.__notas) == 0: 
            return 0
        else:
            return sum(self.__notas) / len(self.__notas)
            
    
    def situacao(self):
        total = self.media( )
        if total >= 7:  
            return 'Aprovado'
        elif total >= 5 and total < 7:
            return 'Recuperação'
        else:
            return 'Reprovado'
            
        
    def __str__(self):
        return f'Aluno: {self.__nome}\nMatrícula: {self.__matricula}\nNotas: {self.__notas}\nMédia: {self.media()}\nSituação: {self.situacao()}'
    