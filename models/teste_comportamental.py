class Teste:
    def __init__(self, perguntas):
        self.perguntas = perguntas
        self.respostas = []
        self.indice_atual = 0

    def get_pergunta_atual(self):
        if self.indice_atual < len(self.perguntas):
            return self.perguntas[self.indice_atual]
        return None

    def responder(self, resposta):
        self.respostas.append(resposta)
        self.indice_atual += 1

    def is_finalizado(self):
        return self.indice_atual >= len(self.perguntas)