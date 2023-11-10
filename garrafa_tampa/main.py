from garrafa import *
from tampa import *
from lista_garrafas import *
menu = """
=========================================
    MENU - Principal
=========================================
    0- Sair
    1- Criar Garrafa
    2- Criar Tampa
    3- Status Garrafa
    4- Status Tampa
    5- Encher a Garrafa
    6- Fechar Garrafa
    7- Tampar a Garrafa
    """
def criando_garrafa():
  volume = int(input("Volume da garrafa: "))
  circunferencia = int(input("Circunferência da garrafa: "))
  garrafa = Garrafa(volume, circunferencia)
  return garrafa
  
def criando_tampa():
  circunferencia = int(input("Circunferência da tampa: "))
  tampa = Tampa(circunferencia)
  return tampa  

def menu_principal():
  while True:
    escolha = int(input(menu + "Escolha: "))
    if escolha == 1:
      garrafa = criando_garrafa()
    elif escolha == 2:
      tampa = criando_tampa()
    elif escolha == 3:  
      if garrafa == None:
        print('Garrafa Não criada! Por favor, crie sua garrafa!!!')
      else:  
        garrafa.__str__()
    elif escolha == 4:
      if tampa == None:
        print('Tampa Não criada! Por favor, crie sua tampa!!!')
      else:
        tampa.__str__()
    elif escolha == 5:
      quantidade = int(input('Quanto ml irá colocar na garrafa? '))
      garrafa.encher(quantidade)
    elif escolha == 6:
      garrafa.fechar()
    elif escolha == 7:
      tampa.__str__()
      if garrafa.__volumeAtual != 0:
        return print('Lamento. Garrafa não está completamente CHEIA. Verefique o status da Garrafa para tampar.')
      else:
        garrafa.receber_tampa(tampa)
        if input('Deseja TAMPAR está garrafa com está TAMPA?[S/N]').upper() == "S":
          garrafa.tampar()
    elif escolha == 0:
      print("Volte sempre!")
      break

menu_principal()

  