from pathlib import Path


def pegar_entrada(texto, opcoes):
    resposta = ''
    while resposta not in opcoes:
        print(texto)
        resposta = input('>>> ')
    return resposta


def corrigir_caminho(caminho):
    if caminho.startswith('~'):
        return Path(caminho).expanduser()
    else:
        return Path(caminho)