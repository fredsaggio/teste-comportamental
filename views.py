# encoding: utf-8
from flask import Flask, render_template, request, redirect, url_for
from models.teste_comportamental import Teste
from models import pergunta_class
import classe

app = Flask(__name__)

perguntas = [
    pergunta_class.Pergunta("Como você prefere resolver um problema inesperado?",
                            ["Analiso todas as opções possíveis antes de decidir",
                             "Tento ouvir o que as pessoas envolvidas têm a dizer",
                             "Improviso uma solução no momento",
                             "Sigo um método ou procedimento já testado"]),

    pergunta_class.Pergunta("O que mais te motiva em um projeto?",
                            ["Resolver desafios intelectuais",
                             "Trabalhar em colaboração com outras pessoas",
                             "Descobrir algo novo e excitante",
                             "Cumprir objetivos claros e organizados"]),

    pergunta_class.Pergunta("Como você costuma reagir a mudanças de última hora?",
                            ["Reavalio tudo rapidamente e ajusto meu plano",
                             "Tento entender como todos estão se sentindo e adapto meu comportamento",
                             "Encaro como uma oportunidade de experimentar algo diferente",
                             "Tento manter as coisas sob controle e seguir o que foi combinado"]),

    pergunta_class.Pergunta("O que você valoriza mais em um ambiente de trabalho?",
                            ["Liberdade para inovar e pensar fora da caixa",
                             "Harmonia e boa comunicação entre as pessoas",
                             "Diversidade de experiências e novas oportunidades",
                             "Organização, regras claras e estabilidade"]),

    pergunta_class.Pergunta("Como você se sente ao assumir a liderança em um grupo?",
                            ["Estou confortável, especialmente se posso guiar com lógica e estratégia",
                             "Gosto de liderar, mas priorizo a harmonia no grupo",
                             "Prefiro liderar em situações dinâmicas e improvisadas",
                             "Prefiro liderar em ambientes bem estruturados e organizados"]),

    pergunta_class.Pergunta("O que te deixa mais satisfeito depois de concluir um projeto?",
                            ["Saber que fiz algo inteligente e eficiente",
                             "Ver que o projeto beneficiou ou conectou as pessoas",
                             "Sentir que aprendi ou vivi algo novo",
                             "Saber que tudo foi feito conforme o planejado"]),

    pergunta_class.Pergunta("Como você prefere aprender algo novo?",
                            ["Pesquiso profundamente e entendo os fundamentos",
                             "Aprendo melhor com conversas e troca de ideias",
                             "Prefiro experimentar e aprender na prática",
                             "Sigo um manual ou instruções detalhadas"]),

    pergunta_class.Pergunta("Como você costuma lidar com conflitos?",
                            ["Analiso a situação e proponho uma solução racional",
                             "Escuto todos os lados e tento buscar um meio-termo",
                             "Tento evitar e sigo em frente sem me envolver muito",
                             "Busco aplicar regras ou normas para resolver a situação"]),

    pergunta_class.Pergunta("Como você organiza suas tarefas diárias?",
                            ["Faço um planejamento estratégico para otimizar meu tempo",
                             "Me organizo em função do que pode ajudar mais as pessoas ao meu redor",
                             "Vou fazendo o que parece mais interessante no momento",
                             "Sigo uma lista ou cronograma bem definido"]),

    pergunta_class.Pergunta("Qual tipo de desafio mais te atrai?",
                            ["Problemas complexos que exigem lógica e análise",
                             "Conflitos ou situações que demandam cooperação",
                             "Aventuras ou oportunidades para explorar algo novo",
                             "Tarefas que exigem foco e organização"]),

    pergunta_class.Pergunta("Como você toma decisões importantes?",
                            ["Baseio-me em dados e lógica para garantir o melhor resultado",
                             "Considero como a decisão vai impactar as pessoas ao meu redor",
                             "Confio na minha intuição e sigo o que parece certo na hora",
                             "Avalio os riscos e sigo um método confiável"]),

    pergunta_class.Pergunta("O que é mais importante para você em uma equipe?",
                            ["Que todos estejam focados na melhor solução possível",
                             "Que exista empatia e comunicação aberta",
                             "Que o ambiente seja dinâmico e divertido",
                             "Que todos cumpram suas funções de maneira eficiente"]),

    pergunta_class.Pergunta("Como você encara prazos apertados?",
                            ["Planejo cuidadosamente para não cometer erros",
                             "Tento manter todos motivados e alinhados",
                             "Dou o meu melhor sem me estressar muito",
                             "Faço o que for necessário para terminar a tempo"]),

    pergunta_class.Pergunta("Qual é o seu tipo de passatempo favorito?",
                            ["Resolver quebra-cabeças ou aprender algo novo",
                             "Participar de atividades sociais e interativas",
                             "Viajar ou explorar lugares diferentes",
                             "Realizar tarefas práticas ou hobbies organizados"]),

    pergunta_class.Pergunta("O que você faz ao iniciar um novo projeto?",
                            ["Planejo os detalhes e analiso possíveis obstáculos",
                             "Busco alinhar as expectativas de todos os envolvidos",
                             "Começo a explorar ideias sem seguir um plano rígido",
                             "Estabeleço um cronograma claro para seguir"]),

    pergunta_class.Pergunta("Como você reage ao fracasso?",
                            ["Reflito sobre o que deu errado e aprendo com isso",
                             "Tento entender o impacto emocional e busco melhorar",
                             "Aceito e sigo em frente em busca de outra oportunidade",
                             "Avalio o que pode ser corrigido para evitar novos erros"]),

    pergunta_class.Pergunta("Como você se sente em relação a regras?",
                            ["Vejo como um guia útil, mas não absoluto",
                             "Respeito-as, mas acredito que podem ser negociadas",
                             "Acho-as limitantes e prefiro mais liberdade",
                             "Acredito que são essenciais para manter a ordem"]),

    pergunta_class.Pergunta("O que te dá mais orgulho em seu trabalho?",
                            ["Saber que usei minha inteligência para fazer algo bem feito",
                             "Ver que ajudei ou inspirei outras pessoas",
                             "Saber que explorei possibilidades novas e divertidas",
                             "Sentir que tudo foi executado conforme o planejado"]),

    pergunta_class.Pergunta("Qual tipo de ambiente mais te deixa confortável?",
                            ["Um local tranquilo onde posso me concentrar em ideias",
                             "Um lugar onde posso conversar e colaborar com outras pessoas",
                             "Um ambiente dinâmico, cheio de novidades",
                             "Um espaço bem organizado e previsível"]),

    pergunta_class.Pergunta("Como você descreveria seu estilo de resolver problemas?",
                            ["Lógico e estratégico, sempre pensando à frente",
                             "Cooperativo e voltado para a solução em grupo",
                             "Espontâneo e adaptável às circunstâncias",
                             "Prático e focado em cumprir o objetivo"])
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
<<<<<<< HEAD
    persona = classe.Exploradores()
    imagem = persona.get_imagem()
    nome = persona.get_nome()
    tipo = persona.get_tipo()
    definicao = persona.get_text()
    positivo1 = persona.get_positivos()[0]
    positivo2 = persona.get_positivos()[1]
    negativo1 = persona.get_negativos()[0]
    negativo2 = persona.get_negativos()[1]
    return render_template("resultado.html", imagem = imagem, nome = nome, tipo = tipo, definicao = definicao, positivo1 = positivo1, negativo1 = negativo1, positivo2 = positivo2, negativo2 = negativo2)
=======
    resultado = teste.resultado_final()
    return render_template("resultado.html", resultado=resultado)
>>>>>>> 3c41f4d4bbedce6b773ad8a0158b758939d22a6d

@app.route("/grafico")
def grafico():
    # Caso você tenha gráficos, como com Matplotlib ou outra ferramenta, implemente aqui
    return render_template("grafico.html")

if __name__ == "__main__":
    app.run(debug=True)