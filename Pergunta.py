class Pergunta:
    def __init__(self, titulo, texto, respostas):
        self.titulo = titulo
        self.texto = texto
        self.respostas = respostas

    def exibir_pergunta(self):

        print(self.texto)
        for chave, valor in self.respostas.items():
            print(f"{chave}: {valor} pontos")

    def calcular_pontos(self, resposta_usuario):

        return self.respostas.get(resposta_usuario, 0)

# Exemplo de uso
pergunta1 = Pergunta("Como você se sentiria em um evento social?", {
    'A': 10,  # Muito confortável
    'B': 5,   # Confortável
    'C': 0    # Desconfortável
})

pergunta1.exibir_pergunta()
resposta = input("Escolha uma resposta (A, B, C): ")
pontos = pergunta1.calcular_pontos(resposta)
print(f"Você ganhou {pontos} pontos.")