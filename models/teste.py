from .pergunta import Pergunta

class TestePersonalidade:
    def __init__(self):
        self.perguntas = [
            Pergunta("Você gosta de trabalhar em equipe?", ["Sim", "Não", "Às vezes"]),
            Pergunta("Prefere atividades criativas?", ["Sim", "Não", "Às vezes"]),
            # Adicione mais perguntas conforme necessário
        ]

    def get_perguntas(self):
        return self.perguntas