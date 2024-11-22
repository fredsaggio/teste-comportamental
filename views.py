from flask import Flask, render_template, request, redirect, url_for
from models.teste_comportamental import Teste
from models.pergunta_class import Pergunta

app = Flask(__name__)

# Definição das perguntas (você pode modificar isso conforme necessário)
perguntas = [
    Pergunta("Qual seu estilo preferido de trabalho?", ["Individual", "Em equipe", "Sob pressão", "Com liberdade"]),
    Pergunta("Você se considera uma pessoa organizada?", ["Sim", "Não", "Às vezes", "Depende"]),
    Pergunta("Como você lida com prazos?", ["Cumpro sempre", "Às vezes atraso", "Não me importo", "Negocio"]),
]

# Inicializando o teste
teste = Teste(perguntas)

@app.route("/")
def home():
    return render_template("inicio.html")

@app.route("/perguntas", methods=["GET", "POST"])
def perguntas():
    pergunta_atual = teste.get_pergunta_atual()
    pergunta_numero = teste.indice_atual + 1  # Exibe o número da pergunta atual

    if request.method == 'POST':
        resposta = request.form.get('opcao')
        if resposta:
            teste.responder(resposta)
            if teste.is_finalizado():
                return redirect(url_for('resultado'))  # Redireciona para a página de resultados
            return redirect(url_for('perguntas'))  # Redireciona para a próxima pergunta

    # Renderiza a pergunta atual no template
    return render_template("perguntas.html", pergunta=pergunta_atual, numero_pergunta=pergunta_numero)

@app.route("/resultado")
def resultado():
    # Aqui você pode processar e mostrar os resultados do teste
    return render_template("resultado.html", respostas=teste.respostas)

@app.route("/grafico")
def grafico():
    # Caso você tenha gráficos, como com Matplotlib ou outra ferramenta, implemente aqui
    return render_template("grafico.html")

if __name__ == "__main__":
    app.run(debug=True)