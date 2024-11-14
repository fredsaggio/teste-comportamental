import os
import matplotlib.pyplot as plt
import numpy as np

class GraficoResultado:
    def __init__(self, resultado):
        self.resultado = resultado

    def gerar_grafico(self):
        categorias = list(self.resultado.keys())
        valores = list(self.resultado.values())

        # Cria o diretório 'static' se ele não existir
        os.makedirs('static', exist_ok=True)

        # Gerar um gráfico de barras horizontais
        plt.figure(figsize=(8, 6))

        # Gerando as cores de forma aleatória para cada barra
        cores = plt.cm.get_cmap('tab20', len(categorias))  # 'tab20' gera um conjunto de cores
        barras = plt.barh(categorias, valores, color=cores(range(len(categorias))))

        # Adicionar título e labels
        plt.title("Distribuição dos Resultados do Teste de Personalidade")
        plt.xlabel('Porcentagem')

        # Adiciona os valores nas barras
        for barra in barras:
            plt.text(barra.get_width() - 0.05, barra.get_y() + barra.get_height() / 2,
                     f'{barra.get_width():.1f}%', va='center', ha='right', color='white')

        # Salva o gráfico
        grafico_path = 'static/grafico_resultado_barras.png'
        plt.tight_layout()
        plt.savefig(grafico_path)
        plt.close()
        return grafico_path