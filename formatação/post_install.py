from os import system as sy
from os import getuid
from pathlib import Path
from os import chdir
from argparse import ArgumentParser


def root() -> bool:
    return getuid() == 0


def verificar_root() -> None:
    if not root(): # é necessário o `which python` pois instala o pipenv
        print(
            'execute este script como root:'
            ' sudo `which python3` post_install.py'
        )
        exit(1)


def main(argumentos):
    verificar_root()
    local = Path(__file__).parent
    chdir(local)

    # atualizando cache
    sy('apt update')

    # instalando programas
    programas = [
        'glade', 'gimp', 'pycodestyle', 'git', 'poppler-utils',
        'bpython', 'net-tools', 'simplescreenrecorder', 'papirus-icon-theme',
        'zeal', 'usb-creator-gtk', 'arc-theme', 'gnome-disk-utility', # ou gparted
        'snapd', 'gnome-software-plugin-snap', 'transmission-gtk',
        'bash-completion', 'gnome-boxes', 'python3-pip', 'libreoffice',
        'zsh', 'curl', 'nano', 'vlc', 'file-roller'
    ]
    # poppler-utils -> pdf
    # gnome-software, loja de programas
    # file-roller para arquivos zip modo gráfico
    # o curl é preciso baixar pois ele será executado ali em baixo
    sy('apt install -y ' + ' '.join(programas))
    sy('snap install video-downloader')
    # woeusb (pendrive bootavel para windows no linux EXCENCIAL)
    # ventoy (pendrive bootabel para qualquer coisa)

    # minhas ferramentas do python
    sy('pip3 install pipenv poetry colored pywal')
    # radon isort coverage pep257 pycodestyle

    chdir(local)
    
    # instalando o oh-my-zsh
    sy(
        'sh -c "$(curl -fsSL https://raw.githu'
        'busercontent.com/robbyrussell'
        '/oh-my-zsh/master/tools/install.sh)"'
    )
    sy('chsh -s $(which zsh)')
    sy(
        'git clone https://github.com/zsh-users/'
        'zsh-syntax-highlighting.git'
    )

    # linkando coisas
    sy('ln -s /usr/bin/bpython3 /usr/bin/bpython')

    # atualizando o sistema
    sy('apt full-upgrade -y')

    # removendo programas e dependências desnecessárias
    sy('apt autoremove -y vim rhythmbox')
    # remover gnome-keyring se ele começar a dar problemas.

    # limpando o sistema caso seja necessário
    sy('apt autoremove -y')

    # instalando a interface de usuário
    if argumentos.interface == 'i3-wm':
        programas = [
            'i3-wm', 'rofi', 'nitrogen', 'picom',
            'lynx', 'lxappearance', 'polybar'
        ]
        # [ncmpcpp mpd mpc]
    elif argumentos.interface == 'xfce4':
        programas = ['xfce4', 'xfce4-goodies']
    sy('apt install -y ' + ' '.join(programas))

    chdir('/tmp')

    # instalando temas para polybar
    sy('git clone --depth=1 https://github.com/adi1090x/polybar-themes.git')
    chdir('/tmp/polybar-themes')
    sy('chmod +x setup.sh')
    sy('./setup.sh')

    chdir('/home/none')

    # instalando os dotfiles do meu repositório.
    config_command = '/usr/bin/git --git-dir=/home/none/.cfg/ --work-tree=/home/none'
    sy('rm .bashrc .zshrc')
    sy('git clone --bare https://github.com/b166erbot/dotfiles /home/none/.cfg')
    sy(config_command + ' checkout')
    # não mudar a linha abaixo. sim, tem dois config
    sy(config_command + ' config --local status.showUntrackedFiles no')

    # copiando o .bash_aliases para o root
    sy('cp .bash_aliases /root')


    # meus scripts
    # sy(f"python3 {local}/../scripts/setup.py install")
    # print(f"python3 {local}/../scripts/setup.py install")
    print('\n' * 3)
    print('baixar o google chrome.deb, visual_studio_code.deb')
    # print('importar os dots. para importar vá no google e pesquise nos favoritos por dot')
    print('instalar manualmente o i3-gaps. pesquise nos favoritos do google que você acha.')
    print(
        'criar um arquivo chamado meu_token.sh '
        'e colocar o token do pendrive nele.'
    )
    print('baixar o executável do telegram pelo site')
    print((
        'instalar os drivers da impressora. pesquisa no ddg o nome da impress'
        'ora'
    ))
    print('remover o firefox. snap remove firefox')
    print('verifique se a instalação do oh-my-zsh foi feita com sucesso')
    print('reinicie o sistema para conferir, se for necessário.')
    # print('instalar o free-ofice e colocar a chave de ativação permanente nele')


if __name__ == '__main__':
    descricao = (
        'programa que instala programas essenciais depois da formatação'
    )
    parser = ArgumentParser(
        usage = 'python3 post_install.py ',
        description=descricao,
    )
    parser.add_argument(
        '--interface', type=str, default='i3-wm',
        choices=['i3-wm', 'xfce4'], required=False,
        help='instala uma interface de usuário para o sistema.'
    )
    argumentos = parser.parse_args()
    main(argumentos)
