from os import chdir, getuid
from pathlib import Path
import json
from _utils import pegar_entrada, corrigir_caminho
from shutil import copy, copytree
from pwd import getpwnam
import re
from itertools import chain


def root() -> bool:
    return getuid() == 0


def remover_arquivos(caminho, extensao, caminhos_remover):
    """Pega o caminho e remove de dentro dele, os quais não foram escolhidos"""
    # a ordem importa, portanto, tem que vir primeiro *.* e depois *
    caminho = Path(str(caminho).replace(extensao, ''))
    arquivos = set(map(
        str, caminho.glob(extensao)
    ))
    if len(caminhos_remover) > 0:
        caminhos_remover = list(
            map(lambda x: str(caminho / x), caminhos_remover)
        )
        arquivos -= set(caminhos_remover)
    return list(arquivos)


def passar_regex(expressao, texto):
    """Passa o regex no texto e retorna os resultados."""
    regex = re.compile(expressao)
    tuplas_de_texto = regex.findall(texto)
    texto_recortado = list(filter(
        lambda texto: bool(texto), chain(*tuplas_de_texto)
    ))
    return texto_recortado


def pegar_caminhos():
    """Pega as entradas do usuário, verifica se existem e as retorna."""
    expressao_regular = '[\"\']([^\"\']+)[\"\']|([^\'\"\s-]+)'
    entradas = []
    while True:
        entrada = input('>>> ')
        if not bool(entrada):
            break
        entrada_recortada = passar_regex(expressao_regular, entrada)
        caminho, _ = corrigir_caminho(entrada_recortada[0])
        if not caminho.exists():
            print('Erro: arquivo ou pasta não existe')
        else:
            entradas.append(entrada)
            if caminho.is_dir():
                print('pasta adicionada')
            elif caminho.is_file():
                print('arquivo adicionado')
    return entradas


def main():
    local = Path(__file__).parent
    chdir(local)

    if root():
        print('o pre_install seria melhor ser executado com o usuário comum')
        exit(1)

    print('*' * 5 + ' Aviso ' + '*' * 5)
    print('você precisa ter o pendrive montado primeiro.')
    print(
        'pra montar, basta abrir o gerenciador de arquivos'
        ' e clicar no pendrive.'
    )
    print('verifique também se o pendrive tem espaço para as músicas.\n')
    while True:
        print('digite o nome do seu usuário')
        usuario = input('>>> ')
        try:
            usuario_final = getpwnam(usuario)
            break
        except KeyError:
            print('Erro: usuário não existe')
            continue

    pasta_home = usuario_final.pw_dir + '/'

    texto = (
        'deseja carregar o arquivo configuracoes.ini ou criar um novo? '
        'responda com "carregar/novo"'
    )
    opcoes = ['carregar', 'novo']
    resposta = pegar_entrada(texto, opcoes)
    if resposta == 'novo':
        print('usagem:', '~/Downloads/*', '~/*.*', '~/Downloads', sep='\n')
        print('~/Downloads - isos "Telegram Desktop" \'teste teste.mp3\'')
        print('"/home/user/teste teste"')
        print('digite abaixo as pastas ou arquivos que deseja copiar:')
        print('(para terminar, precione enter com o texto vazio)')
        entradas = pegar_caminhos()
        with open('configuracoes.json', 'w') as configfile:
            json.dump(entradas, configfile, indent=4)
    else:
        if Path('configuracoes.json').exists():
            with open('configuracoes.json') as configfile:
                entradas = json.load(configfile)
        else:
            print(
                'Erro: o arquivo de configuração não '
                'existe. execute novamente o programa '
                'e crie uma nova lista de pastas/arquivos '
                'a serem copiadas(os)'
            )
            exit(1)
    while True:
        print('digite o caminho para o pendrive ou digite fim para terminar')
        destino_pendrive = Path(input('>>> '))
        if destino_pendrive.name == 'fim':
            exit()
        print('tem certeza que este é o caminho correto? [sim/não/s/n]')
        confirmar = input('>>> ')
        if confirmar in ['sim', 's']:
            break
    destino_pendrive = destino_pendrive / Path('backup')
    if destino_pendrive.exists():
        if destino_pendrive.is_file():
            raise Exception(
                'já existe um arquivo com o nome backup '
                'na pasta do pendrive, favor remover.'
            )
        elif destino_pendrive.is_dir():
            raise IsADirectoryError(
                'o diretório backup já existe no pendrive, favor arrumar.'
            )
    else:
        destino_pendrive.mkdir()
    expressao_regular = '[\"\']([^\"\']+)[\"\']|([^\'\"\s-]+)'
    arquivos_ou_pastas = []
    for entrada in entradas:
        entrada_recortada = passar_regex(expressao_regular, entrada)
        caminho, *caminhos_remover = entrada_recortada
        caminho, extensao = corrigir_caminho(caminho)
        # por obrigatoriedade, o '*.*' vem primeiro que o '*'
        if extensao == '*.*':
            arquivos_ou_pastas += remover_arquivos(
                caminho, '*.*', caminhos_remover
            )
        elif extensao == '*':
            arquivos_ou_pastas += remover_arquivos(
                caminho, '*', caminhos_remover
            )
        else:
            if caminho.is_dir() and bool(len(caminhos_remover)):
                arquivos_ou_pastas += remover_arquivos(
                    caminho, '*', caminhos_remover
                )
            else:
                arquivos_ou_pastas.append(str(caminho))

    for item in arquivos_ou_pastas:
        local_destino = Path(item.replace(pasta_home, ''))
        caminho_final = destino_pendrive / local_destino
        if not caminho_final.parent.exists():
            caminho_final.parent.mkdir(parents=True)
        if Path(item).is_dir():
            copytree(item, caminho_final)
        else:
            copy(item, caminho_final)
    print('arquivos copiados com sucesso.')
    print('agora, alguns lembretes:')
    print('fazer backup dos arquivos da mãe!')


if __name__ == '__main__':
    main()


# tem um problema, se seu colocar mais arquivos no downloads, eles serão ignorados.