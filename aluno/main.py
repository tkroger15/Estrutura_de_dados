from aluno import Aluno

def main():
    aluno_a = Aluno("Rodger", "20227810017")
    aluno_a.adicionar_nota(7)
    aluno_a.adicionar_nota(6)
    aluno_a.adicionar_nota(8)
    print(aluno_a.media())
    print(aluno_a)
    aluno_b = Aluno("Sísifus", "20227810019")
    print(aluno_b)
    aluno_b.adicionar_nota(14)
    
    
if __name__ == '__main__':
    main()
