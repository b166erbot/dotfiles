#!/bin/bash
# https://www.atlassian.com/git/tutorials/dotfiles


# todos os arquivos à serem adicionados não podem conter espaços entre o nome.
# alias config='git --git-dir=/home/none/.cfg/ --work-tree=/home/none'


# $@ no final
function config {
    git --git-dir=/home/none/.cfg/ --work-tree=/home/none add $@
}


config ~/.bash_aliases*
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
config ~/sites_interessantes.txt
config ~/git/.dicas_git
config ~/.config/gtk-3.0/settings.ini
config ~/.config/picom/picom.conf
config ~/.config/rofi/config.rasi
config ~/.arquivos
config ~/.config/rofi/config.rasi
config ~/.config/polybar
config ~/.config/nitrogen
config ~/.config/bspwm
config ~/.config/sxhkd
config ~/meus_programas_do_github.txt
config ~/cola_clamav.txt
config ~/ferramentas_usuario
config ~/bem_vindo
