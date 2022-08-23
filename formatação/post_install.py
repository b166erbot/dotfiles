from os import system as sy
from os import getuid
from pathlib import Path
from os import chdir

from interfaces import interfaces


def root() -> bool:
    return getuid() == 0


def verificar_root() -> None:
    if not root(): # é necessário o `which python` pois instala o pipenv
        print(
            'execute este script como root:'
            ' sudo `which python3` post_install.py'
        )
        exit(1)


def main():
    verificar_root()
    local = Path(__file__).parent
    chdir(local)

    # atualizando cache
    sy('apt update')

    # instalando programas
    programas = [
        'python3-dev', 'glade', 'gimp', 'pycodestyle', 'git', 'poppler-utils',
        'bpython', 'net-tools', 'simplescreenrecorder', 'papirus-icon-theme',
        'zeal', 'usb-creator-gtk', 'arc-theme', 'gnome-disk-utility',
        'snapd', 'gnome-software-plugin-snap', 'transmission-gtk',
        'bash-completion', 'gnome-boxes', 'python3-pip', 'libreoffice',
        'zsh', 'curl', 'nano', 'i3-wm', 'rofi', 'nitrogen', 'picom'
    ] # poppler-utils -> pdf
    # gnome-software, loja de programas
    # o curl é preciso baixar pois ele será executado ali em baixo
    sy('apt install -y ' + ' '.join(programas))
    sy('snap install video-downloader')
    # woeusb (pendrive bootavel para windows no linux EXCENCIAL)
    # ventoy (pendrive bootabel para qualquer coisa)

    # instalando extensões para o atom
    # obs: esta extensão fui eu coloquei
    # sy(f"apm install --packages-file {local}/atom.pacotes")

    # minhas ferramentas do python
    sy('pip3 install pipenv poetry colored')
    # radon isort coverage pep257 pycodestyle

    # configurando zsh
    sy('sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell'
       '/oh-my-zsh/master/tools/install.sh)"')
    sy('chsh -s $(which zsh)')
    sy('cd /home/none && git clone https://github.com/zsh-users/'
       'zsh-syntax-highlighting.git')
    
    # linkando coisas
    sy('ln -s /usr/bin/bpython3 /usr/bin/bpython')

    # atualizando o sistema
    sy('apt full-upgrade -y')

    # removendo programas e dependências desnecessárias
    sy('apt autoremove -y vim firefox rhythmbox')
    # remover gnome-keyring se ele começar a dar problemas.

    # limpando o sistema caso seja necessário
    sy('apt autoremove -y')

    # print('escolha sua(s) interface/configurações')
    # lista = dict(enumerate(interfaces, 1))
    # for numero, interface in lista.items():
    #     print(f"{numero}: {interface}")
    # escolha = int(input('>>> '))
    # while escolha not in lista:
    #     print('coloque um número que esteja na lista')
    #     escolha = int(input('>>> '))
    # comando = interfaces[lista[escolha]]
    # sy(comando)

    # meus scripts
    # sy(f"python3 {local}/../scripts/setup.py install")
    # print(f"python3 {local}/../scripts/setup.py install")
    print('\n' * 3)
    print('importar as configurações dos arquivos dot')
    print(
        'criar um arquivo chamado meu_token.sh '
        'e colocar o token do pendrive nele.'
    )
    print('baixar o executável do telegram pelo site')
    print((
        'instalar os drivers da impressora. pesquisa no ddg o nome da impress'
        'ora'
    ))
    print('baixar o google chrome.deb, visual_studio_code.deb')
    print('instale o oh my zsh')
    # print('instalar o free-ofice e colocar a chave de ativação permanente nele')
    print('executar manualmente a instalação das estenções do atom')


if __name__ == '__main__':
    main()
