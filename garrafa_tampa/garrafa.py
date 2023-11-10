class Garrafa:
    def __init__(self, volume, circunferencia):
        self.__volumeAtual = volume
        self.__volumeTotal = volume
        self.__circunferencia = circunferencia
        self.__aberta = True
        self.__cheio = False
        #self.__tampa = None
    def encher(self, quantidade_liquido):
      self.__volumeAtual -= quantidade_liquido
      if self.__volumeAtual > 0:
        print(f'A garrafa ainda não foi cheia completamente. Falta {self.__volumeAtual}ml para encher.')
      else:
        print('Sua garrafa está cheia!')
        self.__volumeAtual = 0
        self.__cheio = True         
      
    def fechar(self):
      if self.__volumeAtual == 0:
        self.__aberta = False
        return print(f'Está garrafa foi FECHADA...')
      else:
        return print(f'Infelizmente esta garrafa ainda não pode ser fechada pois não está totalmente cheia. \nFaltam {self.__volumeAtual}ml para encher...')
    
    def abrir(self):
      self.__aberta = True
      return print(f'Está garrafa foi ABERTA...')
    
    def __str__(self):
       return print(f'Status desta GARRAFA: \nVolume total: {self.__volumeTotal}ml\nCircunferência: {self.__circunferencia}cm\nAberta? {self.__aberta}\nCheia? {self.__cheio}')
