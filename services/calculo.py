class CalculoResultado:
    def __init__(self, respostas):
        self.respostas = respostas

    def calcular(self):
        # Exemplo: calculando a porcentagem com base nas respostas
        categorias = {"Extrovertido": 0, "Criativo": 0, "Analítico": 0}
        for resposta in self.respostas:
            if resposta == "Sim":
                categorias["Extrovertido"] += 1
            elif resposta == "Não":
                categorias["Analítico"] += 1
            elif resposta == "Às vezes":
                categorias["Criativo"] += 1
        total = len(self.respostas)
        return {k: (v / total) * 100 for k, v in categorias.items()}