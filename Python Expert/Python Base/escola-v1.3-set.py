#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade

Imprimir a lista de crianças agrupadas por sala
que frequenta cada uma das atividades.
"""
__version__ = "1.2"

# Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

# Utilizar tuplas para poder desempacotar o conteúdo
atividades = [
    ("Inglês", aula_ingles),
    ("Música", aula_musica),
    ("Dança", aula_danca),
]

# Listar alunos em cada atividade por sala e desempacotar tuplas
for nome_atividade, atividade in atividades:

    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 40)

# Resolvendo o problema utilizando o set
# Sala1 que tem interseção com a atividade (intersection or &)
    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2).intersection(atividade)

    print("Sala1 ", atividade_sala1)
    print("Sala2 ", atividade_sala2)

    print()
    print("#" * 40)
