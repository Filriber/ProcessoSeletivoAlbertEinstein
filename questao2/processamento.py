#Questao 2 de Data Analysis, processo seletivo Analista de Sistemas Jr Hospital Albert Einstein (Com Modularização)
import pandas as pd

#Destinei essa pagina para colocar todos os processamentos de dados que eu utilizei neste modelo com modularização.

#Aqui é onde utilizo pandas para leitura do arquivo CSV.
def carregar_dados(csv):
    return pd.read_csv("questao2/vendas.csv")

#Criei uma função para calcular o faturamento
def calcular_faturamento(vendas):
    vendas["faturamento"] = vendas["quantidade"] * vendas["preco_unitario"]
    return vendas.groupby("produto")["faturamento"].sum()


#E posteriomente criei duas funções, para poder calcular o minimo e o maximo faturamento
def maior_faturamento(faturamento_por_produto):
    maior = faturamento_por_produto.idxmax()
    valor = faturamento_por_produto[maior]
    return maior, valor
def menor_faturamento(faturamento_por_produto):
    menor = faturamento_por_produto.idxmin()
    valor = faturamento_por_produto[menor]
    return menor, valor