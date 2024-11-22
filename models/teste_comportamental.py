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
        mapeamento_resposta_para_arquétipo = {
            '1': 'Analista',
            '2': 'Diplomata',
            '3': 'Explorador',
            '4': 'Sentinela'
        }

        # Verifica o arquétipo da resposta
        arquétipo = mapeamento_resposta_para_arquétipo.get(resposta)

        if arquétipo:
            self.pontuacoes[arquétipo] += 1

        # Avançar para a próxima pergunta
        self.indice_atual += 1

    def is_finalizado(self):
        return self.indice_atual >= len(self.perguntas)

    def resultado_final(self):
        # Ordenar os arquétipos pelas pontuações
        resultado = max(self.pontuacoes, key=self.pontuacoes.get)
        return resultado