from abc import ABC 
from radom import randint

class Base():
    text = "text"
    nome = "nome"
    def get_text(self):
        return self.text
    def get_nome(self):
        return self.nome

class Analista(Base):
    def __init__(self):
        self.text = "teste"
        self.nome = "Analista"

class Diplomata(Base):
    def __init__(self):
        self.text = "teste"
        self.nome = "Diplomata"

class Sentinela(Base):
    def __init__(self):
        self.text = "teste"
        self.nome = "Sentinela"

class Explorador(Base):
    def __init__(self):
        self.text = "teste"
        self.nome = "Explorador"

