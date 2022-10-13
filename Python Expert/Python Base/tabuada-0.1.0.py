#!/usr/bin/env python
"""Imprime a tabuada do 1 ao 10.

Tabuada do 1
1
2
3
...
-----------------
Tabuada do 2
2
4
...
-----------------
__version__ = "0.1.0"
__author__ = "Dramos"

"""

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1,11)) # list - determina que é pra exibir em lista.
                            # range - exibe um range de numeros

for numero in numeros: # para cada numero em numeros
    print("Tabudada do:",numero) # print Tabuada do numero
    for outro_numero in numeros: # pega a saida do for 1 e faz o mesmo
        print(numero * outro_numero)
    print("-------------")
