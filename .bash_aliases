# ALIASES

alias config='git --git-dir=/home/none/.cfg/ --work-tree=/home/none' # git dotfiles
alias portas_abertas='netstat -atunp'
alias descompactar='tar -xzf'
alias ver_tamanho='du -sh'
alias tempo_de_inicializacao_dos_programas='systemd-analyze blame'
alias git_parar_tracking="config rm --cached"
alias fucking='sudo'
alias abrir='exo-open'
alias variaveis='set'
alias meu_ip="echo $(ifconfig | grep broadcast | awk '{print $2}')"
alias meus_alias='cat ~/.bash_aliases'


# FUNÇÕES

procurar(){
find $1 -name $2
}
