from flask import Flask, render_template, request, redirect, url_for
from models.teste import TestePersonalidade
from services.calculo import CalculoResultado
from services.grafico import GraficoResultado

app = Flask(__name__)
teste = TestePersonalidade()  # Cria o teste com as perguntas

@app.route('/')
def index():
    perguntas = teste.get_perguntas()
    return render_template('index.html', perguntas=perguntas)

@app.route('/submit', methods=['POST'])
def submit():
    respostas = request.form.getlist('resposta')
    resultado = CalculoResultado(respostas).calcular()
    grafico_path = GraficoResultado(resultado).gerar_grafico()
    return render_template('resultado.html', resultado=resultado, grafico_path=grafico_path)

if __name__ == '__main__':
    app.run(debug=True)