import asyncio

async def chamada_rede(nome, tempo):
    print(f"Iniciando {nome}... (espera{tempo}s)")
    await asyncio.sleep(tempo)
    print(f"Finalizando {nome}!")
    return f"{nome} concluída"

