from src.post_install import post_install
from argparse import ArgumentParser


def main():
    descricao = (
        'programa que faz o post install de uma distro derivada de debian'
    )
    usagem = (
        'sudo python3 post_install.py --usuario <usuário> '
        '--pendrive <local do pendrive> '
        '[--interface <interface>]'
    )
    parser = ArgumentParser(
        usage = usagem,
        description=descricao,
    )
    parser.add_argument(
        '--interface', type = str, default = 'i3-wm',
        choices = ['i3-wm', 'xfce4'], required = False,
        help = 'instala uma interface de usuário para o sistema.'
    )
    parser.add_argument(
        '--usuario', type=str, required = True,
        help = 'nome do usuário logado na máquina no momento'
    )
    parser.add_argument(
        '--pendrive', type = str, required = True,
        help = 'local do pendrive para fazer a restauração do backup'
    )
    argumentos = parser.parse_args()
    post_install(argumentos)


main()