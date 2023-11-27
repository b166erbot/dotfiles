from subprocess import call
import os
from pathlib import Path
from configparser import ConfigParser
from argparse import ArgumentParser, Namespace
import tempfile
import signal

from _utils import está_instalado


def signal_handler(signum, frame) -> None:
    raise TimeoutError("Tempo limite esgotado")


def conectar(argumentos: Namespace) -> int:
    local_arquivo_ini = Path(
        '~/não_envie_para_o_github/config_vpn.ini'
    ).expanduser()
    if not local_arquivo_ini.exists():
        local_arquivo_ini_exemplo = (
            Path('~/.arquivos/exemplo_config_vpn.ini').expanduser()
        )
        call(
            "notify-send --urgency=critical".split() +
            [
                f'configure o arquivo "{local_arquivo_ini}" primeiro',
                f"exemplo: {local_arquivo_ini_exemplo}"
            ]
        )
        return 1
    config = ConfigParser()
    config.read(local_arquivo_ini)
    programa = config['vpn1']['programa_linha_de_comando']
    if not está_instalado(programa):
        call(
            "notify-send --urgency=critical".split() +
            [
                f'instale o {programa} para esse programa rodar.'
            ]
        )
        return 1
    arquivo_lock = Path(tempfile.gettempdir(), 'ativar_vpn.lock')
    inicialização = all([not arquivo_lock.exists(), argumentos.inicializacao])
    não_inicialização = not argumentos.inicializacao
    condições = [inicialização, não_inicialização]
    if any(condições):
        arquivo_lock.touch()
        região = config['vpn1']['região']
        try:
            comando = config['vpn1']['comando_conectar']
            status_chamada = call(
                f"{comando} {região}".split()
            )
            if status_chamada == 1:
                nome = config['vpn1']['nome']
                call(
                    "notify-send --urgency=critical".split() +
                    [
                        f"{nome} erro",
                        (
                            f"relogar no {nome} ou mudar de zona. "
                            "Talvez necessário reiniciar"
                        )
                    ]
                )
                return 1
        except Exception as erro:
            nome = config['vpn1']['nome']
            call(
                "notify-send --urgency=critical".split() +
                [
                    f"{nome} erro inesperado",
                    erro
                ]
            )
            return 1
        return 0


def main():
    descrição = 'Ativa a vpn.'
    usagem = 'python3 conectar_vpn.py [-i]'
    parser = ArgumentParser(usage = usagem, description = descrição)
    parser.add_argument(
        '-i', '--inicializacao', action = 'store_true',
        help = 'diz que o programa está executando na inicialização.'
    )
    argumentos = parser.parse_args()
    signal.signal(signal.SIGALRM, signal_handler)
    for _ in range(3):
        signal.alarm(35)
        try:
            status = conectar(argumentos)
            signal.alarm(0)
            exit(status)
        except TimeoutError:
            pass
    call(
        "notify-send --urgency=critical".split() +
        [
            "Não foi possível se conectar com 3 tentativas"
        ]
    )


if __name__ == '__main__':
    main()
