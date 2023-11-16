import json

class Tarefa:
    def __init__(self, titulo, descricao, status, dataCriacao, dataConclusao):
        self.__titulo =  titulo
        self.__descricao = descricao
        self.__status = status
        self.__dataCriacao = dataCriacao
        self.__dataConclusao =  dataConclusao

    def criar_tarefa(self):
        tarefa = {"titulo": self.__titulo, "descricao": self.__descricao, 
        "status": self.__status, "Data de Criação": self.__dataCriacao, "Data de Conclusão": self.__dataConclusao}
        tarefa_criada = json.dumps(tarefa)
    
    def atualizar_status(self):
        pass