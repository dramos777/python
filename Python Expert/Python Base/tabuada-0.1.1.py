#!/usr/bin/env python
"""Imprime a tabuada do 1 ao 10.

---Tabuada do 1---
     1 x 1 = 1
     1 x 2 = 2
     1 x 3 = 3
...
##################
---Tabuada do 2---
     2 x 1 = 2
     2 x 2 = 4
...
##################
"""
__version__ = "0.1.1"
__author__ = "Dramos"

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1, 11)) # list - determina que é pra exibir em lista.
                            # range - exibe um range de numeros

for n1 in numeros: # para cada numero em numeros
    print("{:-^18}".format(f"Tabuada do {n1}"))
    print()
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}"))

    print("#" * 18)
