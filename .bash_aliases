# ALIASES

alias config='git --git-dir=/home/none/.cfg/ --work-tree=/home/none' # git dotfiles
alias portas_abertas='netstat -atunp'
alias ips='ip -c -br a'
alias ver_tamanho='du -sh'
alias tempo_de_inicializacao_dos_programas='systemd-analyze blame'
alias git_parar_tracking="config rm --cached"
alias fucking='sudo'
alias abrir='exo-open'
alias variaveis='set'
alias meu_ip="echo $(ifconfig | grep broadcast | awk '{print $2}')"
alias editar_alias='nano ~/.bash_aliases'
alias ver_processador='inxi -bGI'
alias ver_processos='ps aux'
alias help='run-help'
alias montar_e_transferir_musicas='python3 ~/python\ scripts/scripts/montar_celular_e_transferir_musicas.py'
alias contar_arquivos_pastas='echo "$(ls -a | wc -l) - 2" | bc'
alias ver_atalhos='scripts ver-atalhos'
alias git_ver_rastreados='config ls-tree -r master --name-only'
alias montar_celular='python3 ~/python\ scripts/scripts/_montar_celular.py'

# FUNÇÕES

procurar(){
find $2 -name $1
}

arquivos_ocultos(){
find $1 -name '.*' -type f
}

pastas_ocultas(){
find $1 -name '.*' -type d
}

pastas_vazias(){
find $1 -type d -empty
}

arquivos_vazios(){
find $1 -type f -empty
}

arquivos_executaveis(){
find $1 -perm /a=x -type f
}

descompactar()
{
  if [ -f $1 ] ; then
    case $1 in
      *.tar.bz2)   tar xjf $1   ;;
      *.tar.gz)    tar xzf $1   ;;
      *.bz2)       bunzip2 $1   ;;
      *.rar)       unrar x $1     ;;
      *.gz)        gunzip $1    ;;
      *.tar)       tar xf $1    ;;
      *.tbz2)      tar xjf $1   ;;
      *.tgz)       tar xzf $1   ;;
      *.zip)       unzip $1     ;;
      *.Z)         uncompress $1;;
      *.7z)        7z x $1      ;;
      *.tar.xz)    tar -xf $1   ;;
      *)           echo "'$1' não pode ser extraido via descompactar()" ;;
    esac
  else
    echo "'$1' não é um arquivo válido"
  fi
}
