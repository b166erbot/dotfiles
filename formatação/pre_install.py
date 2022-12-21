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
        print('digite abaixo as pastas ou arquivos que deseja copiar:')
        print('(para terminar, precione enter com o texto vazio)')
        regex = re.compile('[\"\']([^\"\']+)[\"\']|([^\'\"\s-]+)')
        arquivos_ou_pastas = []
        while True:
            caminho = input('>>> ')
            if not bool(caminho):
                break
            caminhos = regex.findall(caminho)
            caminhos = [
                caminho_
                for caminho_ in chain(*caminhos)
                if bool(caminho_)
            ]
            caminho, *caminhos_remover = caminhos
            caminho = corrigir_caminho(caminho)
            if str(caminho).endswith('*.*'):
                arquivos_ou_pastas += remover_arquivos(
                    caminho, '*.*', caminhos_remover
                )
                print('arquivos adicionados')
            elif str(caminho).endswith('*'):
                arquivos_ou_pastas += remover_arquivos(
                    caminho, '*', caminhos_remover
                )
                print('arquivos e pastas adicionados')
            elif caminho.exists():
                if caminho.is_dir():
                    arquivos_ou_pastas += remover_arquivos(
                        caminho, '*', caminhos_remover
                    )
                else:
                    arquivos_ou_pastas.append(str(caminho))
                print('arquivo ou pasta adicionada')
            else:
                print('Erro: arquivo ou pasta não existe')
        with open('configuracoes.json', 'w') as configfile:
            json.dump(arquivos_ou_pastas, configfile, indent=4)
    else:
        if Path('configuracoes.json').exists():
            with open('configuracoes.json') as configfile:
                arquivos_ou_pastas = json.load(configfile)
        else:
            print(
                'Erro: o arquivo de configuração não '
                'existe. execute novamente o programa '
                'e crie uma nova lista de pastas/arquivos '
                'a serem copiadas(os)'
            )
            exit(1)
    while True:
        print('digite o caminho para o pendrive')
        caminho = Path(input('>>> '))
        if caminho.name == 'fim':
            exit()
        print('tem certeza que este é o caminho correto? [sim/não/s/n]')
        confirmar = input('>>> ')
        if confirmar in ['sim', 's']:
            break
    caminho = caminho / Path('backup')
    if caminho.exists():
        if caminho.is_file():
            raise Exception(
                'já existe um arquivo com o nome backup '
                'na pasta do pendrive, favor remover.'
            )
        elif caminho.is_dir():
            raise IsADirectoryError(
                'o diretório backup já existe no pendrive, favor arrumar.'
            )
    else:
        caminho.mkdir()
    for item in arquivos_ou_pastas:
        local_destino = Path(item.replace(pasta_home, ''))
        caminho_final = caminho / local_destino
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


# verificar se há espaço no pendrive antes de copiar.