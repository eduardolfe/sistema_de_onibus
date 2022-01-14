class Onibus:
    def __init__(self,nome_do_onibus,motorista,ponto,fiscal):
        self.nome_do_onibus = nome_do_onibus
        self.motorista = motorista
        self.ponto = ponto
        self.fiscal = fiscal

aux = Onibus('vazio','vazio','vazio','vazio') # variável Global auxiliar

def criar_onibus():
    aux.nome_do_onibus = input('Escreva aqui o nome do ônibus: ')
    print('O ônibus '+aux.nome_do_onibus+' foi criado')
    return aux

def criar_motorista(): 
    aux.motorista = input('Escreva aqui o nome do Motorista: ')
    print('O motorista '+aux.motorista+' foi criado')
    return aux

def criar_ponto():
    aux.ponto = input('Escreva aqui o nome do Ponto: ')
    print('O ponto '+aux.ponto+' foi criado')
    return aux

def criar_fiscal(): 
    aux.fiscal = input('Escreva aqui o nome do Fiscal: ')
    print('O fiscal '+aux.fiscal+' foi criado')

def mostrar_onibus():
    return print('Nome do ônibus: '+aux.nome_do_onibus)

def mostrar_motorista():
    return print('Nome do motorista: '+aux.motorista)

def mostrar_ponto():
    return print('Nome do ponto: '+aux.ponto)

def mostrar_fiscal():
    return print('Nome do fiscal: '+aux.fiscal)

def mudar_onibus():
        var = aux.nome_do_onibus
        aux.nome_do_onibus = input('Escreva o novo nome do ônibus ')
        print('O ônibus '+var+' foi mudado para '+aux.nome_do_onibus)
        return aux

def mudar_motorista(): 
    var =aux.motorista
    aux.motorista = input('Escreva o nome do Motorista ')
    print('O motorista '+var+' foi mudado para '+aux.motorista)
    return aux

def mudar_ponto():
    var = aux.ponto
    aux.ponto = input('Escreva o nome do Ponto ')
    print('O ponto '+var+' foi mudado para '+aux.ponto)
    return aux

def mudar_fiscal(): 
    var = aux.fiscal
    aux.fiscal = input('Escreva o nome do Fiscal ')
    print('O fiscal '+var+' foi mudado para '+aux.fiscal)

def deletar_onibus():
    var = aux.nome_do_onibus
    aux.nome_do_onibus = 'vazio'
    print('O ônibus '+var+' foi deletado')
    return aux

def deletar_motorista():
    var = aux.motorista
    aux.motorista = 'vazio'
    print('O motorista '+var+' foi deletado')
    return aux

def deletar_ponto():
    var = aux.ponto
    aux.ponto = 'vazio'
    print('O ponto '+var+' foi deletado')
    return aux

def deletar_fiscal():
    var = aux.fiscal
    aux.fiscal = 'vazio'
    print('O fiscal '+var+' foi deletado')
    return aux

def main():
    while True:
        print('Aperte 1 para criar um Ônibus')
        print('Aperte 2 para criar um Motorista')
        print('Aperte 3 para criar um Ponto')
        print('Aperte 4 para criar um Fiscal')
        print('Aperte 5 para mostrar o Ônibus')
        print('Aperte 6 para mostrar o Motorista')
        print('Aperte 7 para mostrar o Ponto')
        print('Aperte 8 para mostrar o Fiscal')
        print('Aperte 9 para mudar o Ônibus')
        print('Aperte 10 para mudar o Motorista')
        print('Aperte 11 para mudar o Ponto')
        print('Aperte 12 para mudar o Fiscal')
        print('Aperte 13 para deletar o Ônibus')
        print('Aperte 14 para deletar o Motorista')
        print('Aperte 15 para deletar o Ponto')
        print('Aperte 16 para deletar o Fiscal')
        print('Aperte 17 para Sair do Sistema')
        opcao = int(input('Digite aqui a sua opção: '))
        if opcao == 1:
            criar_onibus()
        if opcao == 2:
            criar_motorista()
        if opcao == 3:
            criar_ponto()
        if opcao == 4:
            criar_fiscal()
        if opcao == 5:
            mostrar_onibus()
        if opcao == 6:
            mostrar_motorista()
        if opcao == 7:
            mostrar_ponto()
        if opcao == 8:
            mostrar_fiscal()
        if opcao == 9:
            mudar_onibus()
        if opcao == 10:
            mudar_motorista()
        if opcao == 11:
            mudar_ponto()
        if opcao == 12:
            mudar_fiscal()
        if opcao == 13:
            deletar_onibus()
        if opcao == 14:
            deletar_motorista()
        if opcao == 15:
            deletar_ponto()
        if opcao == 16:
            deletar_fiscal()
        if opcao == 17:
            print ('Você saiu do Sistema.')
            break



'''def preco_passagem(lista_de_pontos):
    distancia = len(lista_de_pontos)
    passagem_fixa = 0.3
    passagem_final = passagem_fixa*distancia'''


main()


