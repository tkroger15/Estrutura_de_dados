from city import City 


def main():
    japao = City('Japão', 'Tokyo', '30000')
    japao.exibir_fronteira()
    japao.adicionar_pais_fronteira('guine')
    japao.adicionar_pais_fronteira('venezuela')
    japao.exibir_fronteira()
    print(japao)
                                   
    

if __name__ == '__main__':
    main()