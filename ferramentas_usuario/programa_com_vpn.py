from subprocess import call
import os, sys
from pathlib import Path
from configparser import ConfigParser
from argparse import ArgumentParser, Namespace
from threading import Thread
from functools import partial
from queue import Queue

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
sys.path.append(str(Path('~/ferramentas_usuario').expanduser()))


from conectar_vpn import conectar
from desconectar_vpn import desconectar
from _utils import está_instalado


def retornar_local():
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        return Path(sys._MEIPASS)
    else:
        return Path('.')


local_da_execução = retornar_local()
local_arquivo_ini = (
    Path('~/não_envie_para_o_github/config_programas_vpn.ini').expanduser()
)


class Janela:
    def __init__(
        self, config: ConfigParser, argumentos: Namespace, queue: Queue
    ):
        # ---------// criando objetos //---------
        self.builder = Gtk.Builder()
        self.builder.add_from_file(str(local_da_execução / 'interface.glade'))
        self.config = config
        self.argumentos = argumentos
        self.comando = [
            str(Path(
                self.config[argumentos.programa]['executavel']
            ).expanduser())
        ]
        condições = [
            'navegador' in argumentos.programa, argumentos.janela_privada
        ]
        if all(condições):
            self.comando.append(
                self.config[argumentos.programa]['flag_janela_privada']
            )
        self.queue = queue
        
        # ---------// obtendo objetos //---------
        self._janela = self.builder.get_object('janela')
        self._label = self.builder.get_object('label')
        self._botão_ativar = self.builder.get_object('ativar')
        self._botão_desativar = self.builder.get_object('desativar')
        self._botão_abrir = self.builder.get_object('abrir')
        self._botão_cancelar = self.builder.get_object('cancelar')

        # ---------// conectando objetos //---------
        self._janela.connect('destroy', Gtk.main_quit)
        self._botão_ativar.connect('clicked', self.botão_ativar_clicado)
        self._botão_desativar.connect('clicked', self.botão_desativar_clicado)
        self._botão_abrir.connect('clicked', self.botão_abrir_cliclado)
        self._botão_cancelar.connect('clicked', self.botão_cancelar_clicado)

        # ---------// configurando //---------
        nome_programa = config[argumentos.programa]['nome']
        texto = f"O que deseja fazer antes de abrir o {nome_programa}?"
        self._label.set_text(texto)
        self._janela.show_all()

    def botão_ativar_clicado(self, widget) -> None:
        self._janela.hide()
        self.queue.put('ativar')
    
    def botão_desativar_clicado(self, widget) -> None:
        self._janela.hide()
        self.queue.put('desativar')

    def botão_abrir_cliclado(self, widget) -> None:
        self._janela.hide()
        self.queue.put('abrir')
    
    def botão_cancelar_clicado(self, widget) -> None:
        self.queue.put('sair')


def executar_comando_conectar(queue_status: Queue):
    argumentos = Namespace(inicializacao = False)
    status = conectar(argumentos)
    queue_status.put(status)


def executar_comando(comando: list[str], queue: Queue) -> None:
    botão_clicado = queue.get()
    status = None
    queue_status = Queue()
    if botão_clicado == 'ativar':
        for _ in range(3):
            thread_conectar = Thread(
                target = executar_comando_conectar, args = (queue_status,)
            )
            thread_conectar.start()
            thread_conectar.join(timeout = 35)
            if not queue_status.empty():
                status = queue_status.get()
                break
        if status == None:
            call(
                "notify-send --urgency=critical".split() +
                [
                    'Não foi possível se conectar com a vpn.'
                ]
            )
    elif botão_clicado == 'desativar':
        argumentos = Namespace(finalizacao = False)
        desconectar(argumentos)
        status = 0
    condições = [status == 0, botão_clicado == 'abrir']
    if any(condições):
        call(comando)
    Gtk.main_quit()


def main():
    usagem = "[poetry run] python3 programa_com_vpn.py [-jp]"
    descrição = 'pergunta o que fazer com a vpn antes de abrir um programa'
    parser = ArgumentParser(usage = usagem, description = descrição)
    parser.add_argument(
        '-jp', '--janela-privada', action = 'store_true',
        help = 'abre uma janela privada ao invés de uma janela normal'
    )
    parser.add_argument(
        '-p', '--programa', required = True, type = str,
        help = 'programa que está nas configurações para ser aberto'
    )
    argumentos = parser.parse_args()
    if not local_arquivo_ini.exists():
        local_arquivo_ini_exemplo = (
            Path('~/.arquivos/exemplo_config_programas_vpn.ini').expanduser()
        )
        call(
            "notify-send --urgency=critical".split() +
            [
                f'configurar arquivo {local_arquivo_ini} primeiro.',
                
            ]
        )
        exit()
    config = ConfigParser()
    config.read(local_arquivo_ini)
    local_programa = (
        Path(config[argumentos.programa]['executavel']).expanduser()
    )
    condições = [
        local_programa.exists(), está_instalado(str(local_programa))
    ]
    if not any(condições):
        nome = config[argumentos.programa]['nome']
        call(
            "notify-send --urgency=critical".split() +
            [
                f'baixar o {nome} primeiro.',
                (
                    'extraia ele na pasta Downloads caso ele não '
                    'seja um comando.'
                )
            ]
        )
        exit()
    queue = Queue()
    app = Janela(config, argumentos, queue)
    thread_janela = Thread(target = Gtk.main, daemon = True)
    thread_janela.start()
    função = partial(executar_comando, app.comando, queue)
    thread_executar_comando = Thread(target = função)
    thread_executar_comando.start()
    thread_janela.join()


main()