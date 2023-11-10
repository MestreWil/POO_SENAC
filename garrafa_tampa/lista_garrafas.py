from garrafa import *
lista_garrafas = []

def adicionar_garrafa(garrafa):
  lista_garrafas.append(garrafa)

def apagar_garrafa(num_garrafa):
  for garrafa in lista_garrafas:
    if garrafa.num_garrafa == num_garrafa:
      lista_garrafas.remove(garrafa) 

def mostrar_garrafas():
  print(f'Ao todo temos no momento {len(lista_garrafas)} criadas.')
  
  '''for garrafa in range(lista_garrafas):
    mostrar = lista_garrafas[garrafa].__str__()
    return print(f"Lista de Garrafas criadas: {mostrar}")'''