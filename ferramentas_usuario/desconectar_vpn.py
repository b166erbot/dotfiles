from subprocess import call, DEVNULL
from pathlib import Path
from configparser import ConfigParser
from argparse import ArgumentParser, Namespace


def desconectar(argumentos: Namespace):
    local_config_vpn = Path(
        '~/não_envie_para_o_github/config_vpn.ini'
    ).expanduser()
    local_exemplo_config_vpn = Path(
        '~/.arquivos/exemplo_config_vpn.ini'
    ).expanduser()
    if not local_config_vpn.exists():
        call(
            "notify-send --urgency=critical".split() +
            [
                f"configure o arquivo '{local_config_vpn}' primeiro",
                f"exemplo: {local_exemplo_config_vpn}"
            ]
        )
        exit(1)
    local_lock = Path('/tmp/ativar_vpn.lock')
    condições = [
        argumentos.finalizacao, local_lock.exists()
    ]
    if all(condições):
        local_lock.unlink()
    config = ConfigParser()
    config.read(local_config_vpn)
    comando = config['vpn1']['comando_desconectar']
    call(comando.split())


def main():
    usagem = 'python3 desconectar_vpn.py [-f]'
    descrição = 'Desativa a vpn.'
    parser = ArgumentParser(usage = usagem, description = descrição)
    parser.add_argument(
        '-f', '--finalizacao', action = 'store_true',
        help = (
            'diz que o programa está executando na '
            'saída do sistema [logout/shutdown]'
        )
    )
    argumentos = parser.parse_args()
    desconectar(argumentos)


if __name__ == '__main__':
    main()