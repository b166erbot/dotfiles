from os import system as sy
from os import getuid
from pathlib import Path
from os import chdir
from argparse import ArgumentParser
import json
from src.restaurar_backup import restaurar_backup


def root() -> bool:
    return getuid() == 0


def verificar_root() -> None:
    # é necessário o `which python` pois instala o pipenv
    if not root():
        print(
            'execute este script como root:'
            ' sudo `which python3` post_install.py'
        )
        exit()


def post_install(argumentos):
    local = Path(__file__).parent.parent
    chdir(local)

    if Path('sistemas.json').exists():
            with open('sistemas.json') as configfile:
                config = json.load(configfile)
    else:
        print(
            'arquivo configuracoes.json não existe. por favor '
            'execute o pre_install para poder criar um novo'
        )
        exit()

    # atualizando cache
    sy(config[argumentos.sistema]['comando_atualizar'])

    # instalando programas
    # gnome-disk-utility ou gparted
    # poppler-utils -> pdf
    # gnome-software, loja de programas
    # file-roller para arquivos zip modo gráfico
    # o curl é preciso baixar pois ele será executado ali em baixo
    # remover esses comentários acima e colocar em um arquivo de texto?
    sy(
        (
            config[argumentos.sistema]['comando_install']
            + ' '.join(config[argumentos.sistema]['programas'])
        )
    )
    sy('snap install video-downloader')
    # woeusb (pendrive bootavel para windows no linux EXCENCIAL)
    # ventoy (pendrive bootabel para qualquer coisa)

    # minhas ferramentas do python
    sy('pip install pipenv poetry colored pywal')
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
    sy(
        f"ln -s {config[argumentos.sistema]['pasta-bin']}/bpython3 "
        f"{config[argumentos.sistema]['pasta-bin']}/bpython"
    )

    # atualizando o sistema
    # sy('apt full-upgrade -y')

    # removendo programas e dependências desnecessárias
    if argumentos.sistema == 'debian':
        sy('apt autoremove -y vim rhythmbox')
    # remover gnome-keyring se ele começar a dar problemas.

    # limpando o sistema caso seja necessário
    sy(config[argumentos.sistema]['comando_autoremove'])

    # instalando a interface de usuário
    instalar_polybarthemes = False
    programas = [
        'rofi', 'nitrogen', 'picom', 'lxappearance', 'polybar'
    ]
    if argumentos.interface == 'i3':
        programas.append('i3')
        #instalar_polybarthemes = True
        # [ncmpcpp mpd mpc]
    elif argumentos.interface == 'bspwm':
        programas.append('bspwm')
        #instalar_polybarthemes = True
    elif argumentos.interface == 'xfce4':
        programas = ['xfce4', 'xfce4-goodies']
    sy(config[argumentos.sistema]['comando_install'] + ' '.join(programas))

    #chdir('/tmp')

    # instalando temas para polybar
    #if instalar_polybarthemes:
    #    sy('git clone --depth=1 https://github.com/adi1090x/polybar-themes.git')
    #    chdir('/tmp/polybar-themes')
    #    sy('chmod +x setup.sh')
    #    sy('./setup.sh')

    chdir('/home/' + argumentos.usuario)

    # instalando os dotfiles do meu repositório.
    config_command = (
        'git --git-dir=/home/none/.cfg/ --work-tree=/home/none'
    )
    sy('rm .bashrc .zshrc')
    sy('git clone --bare https://github.com/b166erbot/dotfiles /home/none/.cfg')
    sy(config_command + ' checkout')
    # não mudar a linha abaixo. sim, tem dois config
    sy(config_command + ' config --local status.showUntrackedFiles no')

    # linkando o .bash_aliases para o root
    # sy('ln -s .bash_aliases /root')

    chdir(local)
    
    # movendo os arquivos backup do pendrive para seus respectivos lugares
    # su -c "comando" -s /bin/sh nomedoUsuario
    # from subprocess import run
    # run('su none -c ./restaurar_backup.py'.split())
    restaurar_backup(argumentos)

    # meus scripts
    sy("python3 ~/python\ scripts/scripts/setup.py install")
    

    # finalizando.
    print('\n' * 3)
    print('baixar o google chrome.deb, visual_studio_code.deb')
    # print('importar os dots. para importar vá no google e pesquise nos favoritos por dot')
    #print(
    #    'instalar manualmente o i3-gaps. pesquise nos favoritos por'
    #    ' i3-gaps no google que você acha.'
    #)
    print(
        'criar um arquivo chamado meu_token.sh '
        'e colocar o token do pendrive nele.'
    )
    print('baixar o executável do telegram pelo site')
    print(
        'instalar os drivers da impressora. pesquisa no ddg o nome da impress'
        'ora'
    )
    print('remover o firefox. snap remove firefox')
    print('verifique se a instalação do oh-my-zsh foi feita com sucesso')
    print('reinicie o sistema para conferir, se for necessário.')
    print(
        'alterar a imagem de login com o lightdm-gtk-greeter-settings.'
        ' a imagem deve ser colocada no /usr/share/wallpapers com sudo.'
    )
    print(
        'clonar o repositorio das notificações. ele está oculto, '
        'portanto vai precisar de senha'
    )
    print('instalar os programas da função descompactar do aliases')
    # print('instalar o free-ofice e colocar a chave de ativação permanente nele')


def main():
    verificar_root()
    descricao = (
        'programa que faz o post install de uma distro derivada de debian'
    )
    usagem = (
        'sudo python3 post_install.py --usuario <usuário> '
        '--origem-pendrive <local do pendrive> '
        '--sistema <nome do sistema operacioanl rodando no momento> '
        '[--interface <interface>]'
    )
    parser = ArgumentParser(
        usage = usagem,
        description=descricao,
    )
    parser.add_argument(
        '--interface', type = str, default = 'i3',
        choices = ['i3', 'xfce4', 'bspwm'], required = False,
        help = 'instala uma interface de usuário para o sistema.'
    )
    parser.add_argument(
        '--usuario', type=str, required = True,
        help = 'nome do usuário logado na máquina no momento'
    )
    parser.add_argument(
        '--origem-pendrive', type = str, required = True,
        help = 'local do pendrive para fazer a restauração do backup'
    )
    parser.add_argument(
        '--sistema', type = str, required = True,
        choices = ['debian', 'arch-linux'],
        help = 'sistema operacional que está rodando no momento.'
    )
    argumentos = parser.parse_args()
    post_install(argumentos)



# observação: todo "sy" que for adicionado precisa alterar um punhado de testes.