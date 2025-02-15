#Questao 2 de Data Analysis, processo seletivo Analista de Sistemas Jr Hospital Albert Einstein (Com Modularização)
import processamento
import util

#Armazenando o nome do arquivo CSV dentro de uma variavel
ARQUIVO_CSV = "vendas.csv"

#Destinei a "vendas" o nome do DataFrame que iria utilizar para carregar meus dados CSV
vendas = processamento.carregar_dados(ARQUIVO_CSV)
#Por Estetica, resolvi mostrar a minha tabela com todos os dados antes de realizar o processamento dos dados
util.exibir_tabela_inicial(vendas)

#Aqui é onde faço a chamada dos processamentos para calcular quanto foi o faturamento por produto, preço minimo de faturamento e preço maximo!
faturamento_por_produto = processamento.calcular_faturamento(vendas)
maior = processamento.maior_faturamento(faturamento_por_produto)
menor = processamento.menor_faturamento(faturamento_por_produto)

#e por uiltimo, onde busco de "util" as exibições dos meus resultados
util.exibir_resultados(faturamento_por_produto, maior, menor)