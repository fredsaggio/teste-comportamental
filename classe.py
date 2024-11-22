# encoding: utf-8
from random import randint

class base():
    tipo = ""
    text = ""
    nome = "nome"
    pontos_fortes = []
    pontos_fracos = []
    url_imagen = ""
    def get_tipo(self):
        return self.tipo
    def get_text(self):
        return self.text
    def get_nome(self):
        return self.nome
    def get_positivos(self):
        return self.pontos_fortes
    def get_negativos(self):
        return self.pontos_fracos
    def get_imagem(self):
        return self.url_imagen
    def teste(self):
        print(f"{self.get_tipo()}:{self.get_nome()}\n{self.get_text()}\n\nPontos forte:")
        for x in self.get_positivos():
            print("\n" + x)
        print("\nPontos fracos:")
        for x in self.get_negativos():
            print("\n" + x)


class Analista(base):
    tipo = "Analista"
    url_imagen = "images/Analista.svg"
    def __init__(self):
        x = randint(1, 5)
        with open("banco_de_dados/" + self.tipo + ".txt", 'r', encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
        textos = conteudo.split("Texto ")
        partes = textos[x].split("\nPontos Positivos:\n")
        caracte = partes[1].split("\nPontos Negativos:\n")
        texto = partes[0].strip()
        self.pontos_fortes = caracte[0].strip().split("\n")
        self.pontos_fracos = caracte[1].strip().split("\n")
        self.nome = texto.splitlines()[1]
        self.text = texto.splitlines()[2]

class Diplomata(base):
    tipo = "Diplomata"
    url_imagen = "images/diplomata.svg"
    def __init__(self):
        x = randint(1, 5)
        with open("banco_de_dados/" + self.tipo + ".txt", 'r', encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
        textos = conteudo.split("Texto ")
        partes = textos[x].split("\nPontos Positivos:\n")
        caracte = partes[1].split("\nPontos Negativos:\n")
        texto = partes[0].strip()
        self.pontos_fortes = caracte[0].strip().split("\n")
        self.pontos_fracos = caracte[1].strip().split("\n")
        self.nome = texto.splitlines()[1]
        self.text = texto.splitlines()[2]

class Sentinelas(base):
    tipo = "Sentinelas"
    url_imagen = "images/sentinela.svg"
    def __init__(self):
        x = randint(1, 5)
        with open("banco_de_dados/" + self.tipo + ".txt", 'r', encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
        textos = conteudo.split("Texto ")
        partes = textos[x].split("\nPontos Positivos:\n")
        caracte = partes[1].split("\nPontos Negativos:\n")
        texto = partes[0].strip()
        self.pontos_fortes = caracte[0].strip().split("\n")
        self.pontos_fracos = caracte[1].strip().split("\n")
        self.nome = texto.splitlines()[1]
        self.text = texto.splitlines()[2]

class Exploradores(base):
    tipo = "Exploradores"
    url_imagen = "images/explorador.svg"
    def __init__(self):
        x = randint(1, 5)
        with open("banco_de_dados/" + self.tipo + ".txt", 'r', encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
        textos = conteudo.split("Texto ")
        partes = textos[x].split("\nPontos Positivos:\n")
        caracte = partes[1].split("\nPontos Negativos:\n")
        texto = partes[0].strip()
        self.pontos_fortes = caracte[0].strip().split("\n")
        self.pontos_fracos = caracte[1].strip().split("\n")
        self.nome = texto.splitlines()[1]
        self.text = texto.splitlines()[2]

