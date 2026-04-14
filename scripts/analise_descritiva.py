# Scritp Análise Descritiva 

# ===========
# Bibliotecas
# ===========

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ================
# leitura de dados
# ================

df = pd.read_csv('./dados/admissao_alunos_vestibular.csv',sep = ',')


# grafico de barras profissional 

dados = df
categoria = 'admit'


def gbarras(dados, categoria, largura_bar = 0.5):

    # calcular valores
    tabela = dados[categoria].value_counts().reset_index()

    tabela['perc'] = (tabela['count']/sum(tabela['count']))*100

    plt.subplot()

    plt.bar(tabela[categoria], height = tabela['count'], width = largura_bar)
    plt.show()


for i in range(5,55,5):
    print(i,"-", end="")

mat = []
soma = 0

for i in range(3):
    for j in range(3):
        soma = soma + mat[i][j]

x = -1
resultado = 0

for i in range(10):

    while(x < 1):
        x = int(input("Insira um valor: "))
    resultado = resultado*x

    print(resultado)
     
def multiplica(x, y):
    resultado=int()
    resultado= x * y
    return print(resultado)

print(\"Insira dois números. \\n\")

x=int(input()); y=int(input());

multiplica(x,y)