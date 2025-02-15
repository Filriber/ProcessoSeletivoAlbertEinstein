#Questao 4 de Asynchronous Programming, processo seletivo Analista de Sistemas Jr Hospital Albert Einstein (Sem modularização)
import asyncio
import time

async def chamada_rede(nome, tempo):
    print(f"Iniciando {nome}... (espera {tempo}s)")
    await asyncio.sleep(tempo)
    print (f"Finalizando {nome}!")
    return f"{nome} concluida"

async def main():
    inicio = time.time()

    tarefas = [
        chamada_rede("Requisição 1", 3),
        chamada_rede("Requisição 2", 2),
        chamada_rede("Requisição 3", 1)
    ]

    resultado = await asyncio.gather(*tarefas)

    fim = time.time()

    print("\nResultados:", resultado)
    print(f"Tempo total de execução: {fim - inicio:.2f} segundos")

asyncio.run(main())