apt update

LOCAL_SCRIPT="$HOME/python scripts/minhas ferramentas para o sistema/formatação"

# instalando programas
apt install -y sqlite3 python3-gi python3-dev glade gimp gnome-sistem-monitor \
pycodestyle bpython3 net-tools simplescreenrecorder papirus-icon-theme atom \
telegram zeal usb-creator-gtk arc-theme gnome-disk-utility gnome-software \
snapd gnome-software-plugin-snap flatpak gnome-software-plugin-flatpak
# lightdm-gtk-greeter-settings gtk-theme-config

# instalando extensões para o atom
apm install --packages-file "$LOCAL_SCRIPT/atom.pacotes"

# minhas ferramentas do python
pip3 install -y pipenv
# radon isort coverage pep257 pycodestyle

# linkando coisas
ln -s /usr/bin/bpython3 /usr/bin/bpython

# meus scripts
python3 "$LOCAL_SCRIPT/../scripts/setup.py" install

# atualizando o sistema
apt full-upgrade -y

# removendo programas e dependências desnecessárias
# apt remove -y vim

# limpando o sistema caso seja necessário
apt autoremove -y
