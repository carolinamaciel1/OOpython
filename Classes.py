class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao


class Series:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas


vingadores = Filme('Vingadores - guerra infinita', 2018, 160)
glee = Series('Glee', 2010, 6)

print(vingadores.nome)
print(f'Nome: {glee.nome} - Ano: {glee.ano} - Temporadas: {glee.temporadas}')
