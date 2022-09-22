#!/bin/bash
# https://www.atlassian.com/git/tutorials/dotfiles


# todos os arquivos à serem adicionados não podem conter espaços entre o nome.
# alias config='git --git-dir=/home/none/.cfg/ --work-tree=/home/none'


# $@ no final
function config {
    git --git-dir=/home/none/.cfg/ --work-tree=/home/none add $@
}


config ~/.bash_aliases
config ~/.bashrc
config ~/.config/Thunar/accels.scm
config ~/.config/Thunar/uca.xml
config ~/.config/i3/config
config ~/.dotfiles_cola
config ~/.gitconfig
config ~/.gitignore
config ~/.pdbrc
config ~/.pythonrc
config ~/.zshrc
config ~/adicionar_arquivos_config_git.sh
config ~/bem_vindo.py
config ~/formatação/post_install.py
config ~/formatação/pre_install.py
config ~/sites_interessantes.txt
config ~/git/dicas_para_comandos_git.txt
config ~/.config/ncmpcpp/config
config ~/.config/mpd/mpd.conf
config ~/.config/gtk-3.0/settings.ini
