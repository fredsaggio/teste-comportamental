class Teste:
    def __init__(self, perguntas):
        self.perguntas = perguntas
        self.respostas = []
        self.indice_atual = 0
        self.pontuacoes = {
            'Analista': 0,
            'Diplomata': 0,
            'Explorador': 0,
            'Sentinela': 0
        }

    def get_pergunta_atual(self):
        if self.indice_atual < len(self.perguntas):
            return self.perguntas[self.indice_atual]
        return None

    def responder(self, resposta):
        self.respostas.append(resposta)
        # Mapeamento da resposta para o arquétipo
        if resposta == '1':
            self.pontuacoes['Analista'] += 1
        elif resposta == '2':
            self.pontuacoes['Diplomata'] += 1
        elif resposta == '3':
            self.pontuacoes['Explorador'] += 1
        elif resposta == '4':
            self.pontuacoes['Sentinela'] += 1
        self.indice_atual += 1

    def is_finalizado(self):
        return self.indice_atual >= len(self.perguntas)

    def resultado_final(self):
        # Ordenar os arquétipos pelas pontuações
        resultado = max(self.pontuacoes, key=self.pontuacoes.get)
        return resultado