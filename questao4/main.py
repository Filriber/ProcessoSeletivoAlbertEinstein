import asyncio
import time
from tarefas import chamada_rede

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

if __name__ == "__main__":
    asyncio.run(main())






