#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade

Imprimir a lista de crianças agrupadas por sala
que frequenta cada uma das atividades.
"""
__version__ = "1.0"

# Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

# Listar alunos em cada atividade por sala
aula_ingles_sala1 = []
aula_ingles_sala2 = []

for aluno in aula_ingles:
    if aluno in sala1:
        aula_ingles_sala1.append(aluno)
    elif aluno in sala2:
        aula_ingles_sala2.append(aluno)
print("Inglês sala1 ", aula_ingles_sala1)
print("Inglês sala2 ", aula_ingles_sala2)

aula_musica_sala1 = []
aula_musica_sala2 = []

for aluno in aula_musica:
    if aluno in sala1:
        aula_musica_sala1.append(aluno)
    elif aluno in sala2:
        aula_musica_sala2.append(aluno)
print("Música sala1 ", aula_musica_sala1)
print("Música sala2 ", aula_musica_sala2)

aula_danca_sala1 = []
aula_danca_sala2 = []

for aluno in aula_danca:
    if aluno in sala1:
        aula_danca_sala1.append(aluno)
    elif aluno in sala2:
        aula_danca_sala2.append(aluno)
print("Dança sala1 ", aula_danca_sala1)
print("Dança sala2 ", aula_danca_sala2)
