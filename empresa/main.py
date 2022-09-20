from polimorfismo import pessoa as p 

def main():
    enginer = p.Fornecedor('luquinhas', 'sao vicente', '4002', 3000, 2000)
    gi = p.Operario('gi', 'zeu', '2345', '324', 3000, 20, 30, 900)
    print(gi.CalcularSalario())
    
    
if __name__ == '__main__': 
    main()