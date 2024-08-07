# ~/.profile: executed by the command interpreter for login shells.
# This file is not read by bash(1), if ~/.bash_profile or ~/.bash_login
# exists.
# see /usr/share/doc/bash/examples/startup-files for examples.
# the files are located in the bash-doc package.

# the default umask is set in /etc/profile; for setting the umask
# for ssh logins, install and configure the libpam-umask package.
#umask 022

# if running bash
if [ -n "$BASH_VERSION" ]; then
    # include .bashrc if it exists
    if [ -f "$HOME/.bashrc" ]; then
	. "$HOME/.bashrc"
    fi
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi

# rodando o agent ssh e o gnome keyring
#gnome-keyring-daemon --replace --components=pkcs11,secrets,ssh --control-directory=/run/user/1000/keyring &
eval "$(ssh-agent -s)"
: "${XDG_RUNTIME_DIR:=/run/user/$UID}"
export SSH_AUTH_SOCK=$XDG_RUNTIME_DIR/keyring/ssh


# alterando o tema do gtk
export GTK_THEME=Adwaita-dark
. "$HOME/.cargo/env"

# configurando o qt para ficar no modo dark.
# necessário instalar o programa qt5-style-plugins e configurar a linha
# style=gtk2
export QT_QPA_PLATFORMTHEME=qt5ct
