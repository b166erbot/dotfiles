#!/bin/bash
# https://www.atlassian.com/git/tutorials/dotfiles

# todos os arquivos à serem adicionados não podem conter espaços entre o nome.

# alias config='git --git-dir=/home/none/.cfg/ --work-tree=/home/none'

function config {
    git --git-dir=/home/none/.cfg/ --work-tree=/home/none $@
}


config add ~/.bash_aliases
config add ~/.bashrc
config add ~/.config/Thunar/accels.scm
config add ~/.config/Thunar/uca.xml
config add ~/.config/i3/config
config add ~/.dotfiles_cola
config add ~/.gitconfig
config add ~/.gitignore
config add ~/.pdbrc
config add ~/.pythonrc
config add ~/.zshrc
config add ~/adicionar_arquivos_config_git.sh
config add ~/bem_vindo.py
config add ~/formatação/interfaces.py
config add ~/formatação/post_install.py
config add ~/formatação/pre_install.py
config add ~/sites_interessantes.txt
config add ~/git/dicas_para_comandos_git.txt
config add ~/.config/ncmpcpp/config
config add ~/.config/mpd/mpd.conf
config add ~/.config/gtk-3.0/settings.ini