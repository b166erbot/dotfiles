from os import getuid
from argparse import ArgumentParser
from fazer_backup import fazer_backup


def root() -> bool:
    return getuid() == 0


def main(argumentos):
    if root():
        print('o pre_install seria melhor ser executado com o usuário comum')
        exit(1)

    fazer_backup(argumentos)
    print('agora, alguns lembretes:')
    print('fazer backup dos arquivos da mãe!')


if __name__ == '__main__':
    descricao = (
        'programa que faz o pre install de uma distro derivada de debian'
    )
    usagem = (
        'python3 pre_install.py --usuario <usuário> --destino-pendrive '
        '<local do pendrive> [--config-arquivo <carregar/novo>]'
    )
    parser = ArgumentParser(
        usage = usagem,
        description = descricao
    )
    parser.add_argument(
        '--usuario', type=str, required = True,
        help = 'nome do usuário logado na máquina no momento'
    )
    parser.add_argument(
        '--destino-pendrive', type=str, required = True,
        help = 'pendrive de destino para fazer o backup'
    )
    parser.add_argument(
        '--config-arquivo', type=str, required = False,
        default = 'novo', choices = ['novo', 'carregar'],
        help = 'arquivo de configuração a ser carregado'
    )
    argumentos = parser.parse_args()
    main(argumentos)