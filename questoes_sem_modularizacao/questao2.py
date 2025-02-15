#Questao 2 de Data Analysis, processo seletivo Analista de Sistemas Jr Hospital Albert Einstein (Sem modularização)
import pandas as pd

#Resolvi permanecer com esse algoritmo sem modularização apenas como exemplo, porem o mais correto é com a modularização!

#Nesse trecho é onde a biblioteca Pandas faz a leitura do meu CSV e logo a baixo eu mostro ela no terminal.
vendas = pd.read_csv("questao2/vendas.csv")
print(vendas)
print("\n")

#Com o meu DataFrame sendo representado por vendas, aqui é o processo de fazer a contagem do meu faturamento e armazenar em uma nova coluna da tabela.
vendas["faturamento"] = vendas["quantidade"] * vendas ["preco_unitario"]
faturamento_por_produto = vendas.groupby("produto")["faturamento"].sum()
#Logo em seguida faço um print do faturamento dos produtos, e utilizei o (to_string(index=true)) para ocultar informações desnecessarias.
print("Faturamento total por produto:\n")
print(faturamento_por_produto.to_string(index=True))

#Por fim essa é a parte que eu utilizo idxmax e idxmin para pegar o faturamento minimo e o faturamento maximo e distinguir qual produto alcançou esses dois pontos.
maior_faturamento = faturamento_por_produto.idxmax()
print(f"\n o Produto com maior faturamento foi: ({maior_faturamento}) no valor de R${faturamento_por_produto[maior_faturamento]:.2f}")

menor_faturamento = faturamento_por_produto.idxmin()
print(f"\n o Produto com o menor faturamento foi: ({menor_faturamento}) no valor de R${faturamento_por_produto[menor_faturamento]:.2f}")