from time import sleep

class ContaCorrente:
    nome_contas = []
    numero_contas = []
    def __init__(self, nome, numero_conta):
        self.nome = nome 
        self.numero_conta = numero_conta
        self.saldo = 0 
        self.nome_contas.append(self.nome)
        self.numero_contas.append(self.numero_conta) 
        
        
    def banco(self):
        self.__cabecalho()
        escolha = 0 
        while escolha != 4:
            escolha = int(input('O que você deseja Fazer? '))
            if escolha == 1:
                valor = int(input('Qual valor deseja depositar? '))
                NumeroConta = int(input('Confirme o número da sua conta:'))
                if NumeroConta not in self.numero_contas:
                    print('Essa conta não pertence ao nosso banco. Você será bloqueado por 5 minutos.')
                    sleep(5)
                else:
                    self.__depositar(valor)
            elif escolha == 2:
                valor = int(input('Qual valor deseja sacar? '))
                NumeroConta = int(input('Confirme o número da sua conta:'))
                if NumeroConta not in self.numero_contas:
                    print('Essa conta não pertence ao nosso banco. Você será bloqueado por 5 minutos.')
                    sleep(5)
                else:
                    self.__sacar(valor)
            elif escolha == 3:
                NumeroConta = int(input('Confirme o número da sua conta:'))
                if NumeroConta not in self.numero_contas:
                    print('Essa conta não pertence ao nosso banco. Você será bloqueado por 5 minutos.')
                    sleep(5)
                else:
                    self.__dados()
            elif escolha == 4:
                break 
            else:
                print('Número incorreto. Tente novamente!')
            print('-' * 30)
        print('Obrigado por usar o nosso banco! Volte sempre!')
            
    def __depositar(self, valor):
        self.saldo += valor
        print(f'Deposito realizado com sucesso.')
            
    def __sacar(self, valor):
        if valor > self.saldo:
            print(f'Transferência negada. Saldo insuficiente.')
        else:
            self.saldo -= valor 
            print(f'Transferencia realizada.')
    def __dados(self):
        print(f'Nome: {self.nome}\nNúmero da conta: {self.numero_conta}\nSaldo da conta: R${self.saldo :.2f}')
    
    def __cabecalho(self):
        print('-' * 30)
        print('Banco do Brasil'.center(30))
        print('-' * 30)
        print('''1-Depositar\n2-Sacar\n3-Dados\n4-Sair''')
        print('-' * 30)