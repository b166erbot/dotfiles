#!/usr/bin/python3
from _utils import pegar_entrada
from shutil import copy, copytree, rmtree
from pathlib import Path
from pwd import getpwnam
from os import environ


def main():
    print(f'executando como usuario {environ["USER"]}')
    print('*' * 5 + ' Aviso ' + '*' * 5)
    print('você precisa ter o pendrive montado primeiro.')
    print(
        'pra montar, basta abrir o gerenciador de arquivos'
        ' e clicar no pendrive.\n'
    )
    pergunta = (
        'deseja copiar os arquivos de backup para os devidos lugares? '
        '(necessita ter executado o pre_install.py antes) sim/não'
    )
    opcoes = ['sim', 'não', 'nao', 's', 'n']
    resposta = pegar_entrada(pergunta, opcoes)
    if resposta in ['sim', 's']:
        while True:
            print('digite o nome do usuário')
            usuario = input('>>> ')
            try:
                usuario_final = getpwnam(usuario)
                break
            except KeyError:
                print('Erro: usuário não existe')
        
        pasta_home = Path(usuario_final.pw_dir)

        while True:
            print('digite o caminho para o pendrive')
            caminho = Path(input('>>> '))
            print('tem certeza que este é o caminho correto? [sim/não/s/n]')
            confirmar = input('>>> ')
            if confirmar in ['sim', 's']:
                break
        caminho = caminho / Path('backup')
        if not caminho.exists():
            print(
                f'Erro: não existe o caminho {caminho}'
                'favor rodar o pre_install.py.'
            )
            exit(1)
        for item in caminho.glob('*'):
            if item.is_file():
                copy(item, pasta_home / item.relative_to(caminho))
            elif item.is_dir():
                copytree(
                    item, pasta_home / item.relative_to(caminho),
                    dirs_exist_ok=True
                )
        rmtree(caminho)
        print('arquivos e pastas movidos com sucesso!')



if __name__ == '__main__':
    main()