class City:
    def __init__(self, nome, capital, dimensao):
        self.nome = nome 
        self.capital = capital 
        self.dimensao = dimensao 
        self.__paises_fronteira = []
        
    def adicionar_pais_fronteira(self, pais):
        if pais not in self.__paises_fronteira:
            self.__paises_fronteira.append(pais)
    
    def exibir_fronteira(self):
        if len(self.__paises_fronteira) > 0:
            for c in range(len(self.__paises_fronteira)):
                print(f'{c+1} {self.__paises_fronteira[c]}')
        else:
            print('Não foi inserido nenhum país')
        
    @property
    def paises_fronteira(self):
        return self.__paises_fronteira
    
    @property 
    def nome(self):
        return self.__nome 
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def capital(self):
        return self.__capital
    
    @capital.setter
    def capital(self, capital):
        self.__capital = capital
        
    @property
    def dimensao(self):
        return self.__dimensao 
    
    @dimensao.setter
    def dimensao(self, dimensao):
        self.__dimensao = dimensao
        
    def __str__(self):
        return f'País: {self.__nome}\nCapital: {self.__capital}\nDimensões: {self.__dimensao}\nPaíses que fazem fronteira: {", ".join(self.__paises_fronteira)}'
        