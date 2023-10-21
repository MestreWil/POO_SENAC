from classes import *
from lista_cartoes import *
from lista_clientes import *

def inicializa_cartoes():
    criar_cartoes(20)

def entrada():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    cartao_cli = get_cartao()
    if cartao_cli:
        cartao_cli.ativar_cartao()
        cliente = Convidado(nome, telefone, cartao_cli)
        adicionar_cliente(cliente)

def consumo(cardapio):
    while True:
        pedido = Pedido()
        pedido.escolher_item(cardapio)
        cartao_cliente = ler_cartao()
        if cartao_cliente:
            cartao_cliente.adicionar_pedido(pedido)
            if input("Escolher outro item s/n? ").upper() != "S":
                break

def encerramento():
    cartao_cliente = ler_cartao()
    cartao_cliente.conferir_itens()
    if input("Confirma pagamento s/n? ").upper() == "S":
        liberar_cliente(cartao_cliente)
        liberar_cartao(cartao_cliente)
        input("OK. Pagamento Confirmado. Cartão liberado. Enter")
    else:
        input("Pagamento Cancelado. Enter")


def popular_cardapio(cardapio, lista_itens, lista_precos):
    for ind in range(len(lista_itens)):
        cardapio.inserir_itens(lista_itens[ind], lista_precos[ind])


"função inicializa_menu utilizando arquivo JSON"
def inicializa_menu():

    import json
    arquivo = open("arqmenu.json", "r")
    dic_temp = json.load(arquivo)
    arquivo.close()
    cardapio = Cardapio()
    popular_cardapio(cardapio, list(dic_temp.keys()), list(dic_temp.values()))
    return cardapio

def ler_cartao():
    num_cartao = input("Digite número Cartão: ")
    return get_cartao_cliente(num_cartao)

def finalizar_comanda():
    cartao_cliente = ler_cartao()
    cartao_cliente.conferir_itens()
    if input("Confirma pagamento s/n? ").upper() == "S":
        liberar_cliente(cartao_cliente)
        liberar_cartao(cartao_cliente)
        input("OK. Pagamento Confirmado. Cartão liberado. Enter")
    else:
        input("Pagamento Cancelado. Enter")

    print(len(lista_clientes))
    for c in lista_de_cartoes:
        print("  > ",c.numero, len(c.itens_consumo))


menu = """
=========================================
    MENU - Principal
=========================================
    0- Exit
    1- Cadastrar Cliente
    2- Realizar um Pedido
    3- Finalizar a Comanda 
    4- Gerenciar Menu
    5 - Cancelar Pedido
    """
# OBS. Fazer o Cancelar Pedido
def cancelar_pedido():
     while True:
        cartao_cliente = ler_cartao()
        if cartao_cliente:
            cartao_cliente.conferir_itens()
            escolha = int(input('Digite o número do pedido que deseja apagar pela ordem: '))
            cartao_cliente.remover_pedido(escolha)
            if input("Escolher outro item s/n? ").upper() != "S":
                break


def menu_principal():
    cardapio = inicializa_menu()    
    inicializa_cartoes()            
    while True:
        print("\n"*20)
        escolha = input(menu + "Escolha: ")
        if escolha == "0":
            break
        elif escolha == "1":
            entrada()
        elif escolha == "2":
            consumo(cardapio)
        elif escolha == "3":
            finalizar_comanda()
        elif escolha == "5":
            cancelar_pedido()


if __name__ == "__main__":
    menu_principal()

