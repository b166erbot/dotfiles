#!/usr/bin/python3
from _utils import pegar_entrada
from shutil import copy, copytree, rmtree, chown
from pathlib import Path
from pwd import getpwnam
from os import walk
from argparse import ArgumentParser


def caminhar(caminho):
    arquivos_e_pastas = []
    for local, pastas, arquivos in walk(caminho):
        for item in pastas + arquivos:
            arquivos_e_pastas.append(Path(local) / Path(item))
    return arquivos_e_pastas


def mudar_dono(caminhos, dono, grupo):
    for caminho in caminhos:
        chown(str(caminho), dono, grupo)


def restaurar_backup(argumentos):
    print('*' * 5 + ' Aviso ' + '*' * 5)
    print('você precisa ter o pendrive montado primeiro.')
    print(
        'pra montar, basta abrir o gerenciador de arquivos'
        ' e clicar no pendrive.\n'
    )
    resposta = pegar_entrada('está pronto?', ['sim', 's', 'não', 'nao', 'n'])
    if resposta.lower() in ['nao', 'não', 'n']:
        exit(1)
    try:
        usuario_final = getpwnam(argumentos.usuario)
    except KeyError:
        print('Erro: usuário não existe')
        exit(1)
    pasta_home = Path(usuario_final.pw_dir)

    caminho = argumentos.origem_pendrive / Path('backup')
    if not caminho.exists():
        print(
            f'Erro: não existe o caminho {caminho}'
            'favor rodar o pre_install.py.'
        )
        exit(1)
    for item in caminho.glob('*'):
        item_destino = pasta_home / item.relative_to(caminho)
        if item.is_file():
            copy(item, item_destino)
            chown(item, )
        elif item.is_dir():
            copytree(
                item, item_destino,
                dirs_exist_ok=True
            )
            mudar_dono(
                caminhar(item_destino),
                argumentos.usuario,
                argumentos.usuario
            )
    rmtree(caminho)
    print('arquivos e pastas movidos com sucesso!')



if __name__ == '__main__':
    usagem = (
        'python3 restaurar_backup.py --usuario <usuário> '
        '--origem-pendrive <local do pendrive>'
    )
    parser = ArgumentParser(
        usage = usagem
    )
    parser.add_argument(
        '--usuario', type=str, required = True,
        help = 'nome do usuário logado na máquina no momento'
    )
    parser.add_argument(
        '--origem-pendrive', type = str, required = True,
        help = 'local do pendrive para fazer a restauração do backup'
    )
    argumentos = parser.parse_args()
    restaurar_backup(argumentos)