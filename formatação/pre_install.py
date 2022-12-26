from src.pre_install import pre_install
from argparse import ArgumentParser


def main():
    descricao = (
        'programa que faz o pre install de uma distro derivada de debian'
    )
    usagem = (
        'python3 pre_install.py --usuario <usuário> --pendrive '
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
        '--pendrive', type=str, required = True,
        help = 'pendrive de destino para fazer o backup'
    )
    parser.add_argument(
        '--config-arquivo', type=str, required = False,
        default = 'novo', choices = ['novo', 'carregar'],
        help = 'arquivo de configuração a ser carregado'
    )
    argumentos = parser.parse_args()
    pre_install(argumentos)


main()