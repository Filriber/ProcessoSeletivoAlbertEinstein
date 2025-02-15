#Questao 2 de Data Analysis, processo seletivo Analista de Sistemas Jr Hospital Albert Einstein (Com Modularização)

#Destinei esse arquivo apenas para printar os meus resultados no terminal
def exibir_tabela_inicial(vendas):
    print("Tabela com todos os produtos!\n")
    print(vendas.to_string(index=True))

def exibir_resultados( faturamento_por_produto, maior, menor):
    print("\nFaturamento total por produto:\n")
    print(faturamento_por_produto.to_string(index=True))

    print(f"\nO produto com maior faturamento foi: ({maior[0]}) no valor de R${maior[1]:.2f}")
    print(f"\nO produto com menor faturamento foi: ({menor[0]}) no valor de R${menor[1]:.2f}\n")
