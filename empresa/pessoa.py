from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, endereco, telefone):
        self.nome = nome 
        self.endereco = endereco 
        self.telefone = telefone 
        
    @property 
    def nome(self):
        return self.__nome 
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome 
        
    @property 
    def endereco(self):
        return self.__endereco 
    
    @endereco.setter 
    def endereco(self, endereco):
        self.__endereco = endereco 
        
    @property
    def telefone(self):
        return self.__telefone 
    
    @telefone.setter 
    def telefone(self, telefone):
        self.__telefone = telefone 

class Fornecedor(Pessoa):
    def __init__(self, nome, endereco, telefone, valor_credito, valor_divida):
        super().__init__(nome, endereco, telefone)
        self.valor_credito = valor_credito
        self.valor_divida = valor_divida
        
    @property 
    def valor_credito(self):
        return self.__valor_credito 
    
    @valor_credito.setter
    def valor_credito(self, valor_credito):
        self.__valor_credito = valor_credito
        
    @property
    def valor_divida(self):
        return self.__valor_divida
    
    @valor_divida.setter
    def valor_divida(self, valor_divida):
        self.__valor_divida = valor_divida
        
    def obter_saldo(self):
        return f"Saldo de: R${self.__valor_credito - self.__valor_divida :.2f}"
    
class Empregado(Pessoa):
    def __init__(self, nome, endereco, telefone, codigo_setor, salario_base, imposto):
        super().__init__(nome, endereco, telefone)
        self.codigo_setor = codigo_setor 
        self.salario_base = salario_base 
        self.imposto = imposto 
        
    @property
    def codigo_setor(self):
        return self.__codigo_setor 
    
    @codigo_setor.setter
    def codigo_setor(self, codigo_setor):
        self.__codigo_setor = codigo_setor
        
    @property 
    def salario_base(self):
        return self.__salario_base 
    
    @salario_base.setter 
    def salario_base(self, salario_base):
        self.__salario_base = salario_base     
    
    @property 
    def imposto(self):
        return self.__imposto
    
    @imposto.setter 
    def imposto(self, imposto):
        self.__imposto = imposto    
        
    @abstractmethod
    def CalcularSalario(self):
        return f'R${self.salario_base - (self.salario_base * self.imposto / 100) :.2f}'
    
class Administrador(Empregado):
    def __init__(self, nome, endereco, telefone, codigo_setor, salario_base, imposto, ajuda_de_custo):
        super().__init__(nome, endereco, telefone, codigo_setor, salario_base, imposto) 
        self.ajuda_de_custo = ajuda_de_custo 
        
    @property
    def ajuda_de_custo(self):
        return self.__ajuda_de_custo
    
    @ajuda_de_custo.setter
    def ajuda_de_custo(self, ajuda_de_custo):
        self.__ajuda_de_custo = ajuda_de_custo 
        
    def CalcularSalario(self):
        return f'R${(self.salario_base - (self.salario_base * self.imposto / 100)) + self.ajuda_de_custo :.2f}'
    
class Operario(Empregado):
    def __init__(self, nome, endereco, telefone, codigo_setor, salario_base, imposto, comicao, valor_producao):
        super().__init__(nome, endereco, telefone, codigo_setor, salario_base, imposto)
        self.valor_producao = valor_producao
        self.comicao = comicao 
        
    @property
    def valor_producao(self):
        return self.__valor_producao
    
    @valor_producao.setter
    def valor_producao(self, valor_producao):
        self.__valor_producao = valor_producao 
        
    @property
    def comicao(self):
        return self.__comicao
    
    @comicao.setter
    def comicao(self, comicao):
        self.__comicao = comicao 
        
    def __calcular_comicao(self):
        return (self.valor_producao * self.comicao / 100)
        
    def CalcularSalario(self):
        return f'R${(self.salario_base - (self.salario_base * self.imposto / 100)) + self.__calcular_comicao() :.2f}'