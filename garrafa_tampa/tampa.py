class Tampa:
  def __init__(self, circunferencia):
    self.__circunferencia = circunferencia
    self.__encaixada = False
        
  def tampar(self, circunferencia_garrafa):
    if self.__circunferencia == circunferencia_garrafa:
      self.__encaixada = True
      return "Garrafa TAMPADA"
    else:
      return "Não foi possivel tampar a garrafa, pois há incompatibilidade nas circunferências."
            
  def destampar(self):
    if self.__encaixada == True:
      self.__encaixada = False
      return "Garrafa destampada"
    else:
      return 'Essa Garrafa ainda não foi tempada...'
        
  def __str__(self):
    return print(f"Status desta Tampa:\nCircunferência: {self.__circunferencia}cm\nEm uso? {self.__encaixada}")
        
  def tampa_tampada(self):
    if self.__encaixada == True:
      return 'Esta tampa já está sendo usada.'
    return 'Tampa livre para usar.'
        