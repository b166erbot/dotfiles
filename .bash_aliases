# ALIASES

alias config='git --git-dir=/home/none/.cfg/ --work-tree=/home/none' # git dotfiles
alias portas_abertas='ss -atunpl'
alias ips='ip -c -br a'
alias ver_tamanho='du -sh'
alias tempo_de_inicializacao_dos_programas='systemd-analyze blame'
alias git_parar_tracking='config rm --cached -r'
alias fucking='sudo'
alias abrir='exo-open'
alias variaveis='set'
alias meu_ip='ip route get 1 | awk "{print \$7}"'
alias editar_alias='nano ~/.bash_aliases'
alias editar_alias_debian='nano ~/.bash_aliases_debian'
alias editar_alias_arch='nano ~/.bash_aliases_arch'
alias ver_processador='inxi -bGI'
alias ver_processos='ps aux'
alias help='run-help'
alias montar_e_transferir_musicas='python3 ~/python\ scripts/scripts/montar_celular_e_transferir_musicas.py'
alias contar_arquivos_pastas='echo "$(ls -a | wc -l) - 2" | bc'
alias ver_atalhos='scripts ver-atalhos'
alias git_ver_rastreados='config ls-tree -r master --name-only'
alias montar_celular='python3 ~/python\ scripts/scripts/_montar_celular.py --ip 3'
alias substituir='mv -f'
alias chat='shell-genie ask'
alias mover_e_alterar_dono='fucking `which scripts` mover-e-alterar-dono'
alias ver_arquitetura_pro='uname -m'
alias atualizar_shell='source ~/.zshrc'
alias remover_exif='mogrify -strip'
alias trocar_usuario='dm-tool switch-to-greeter'
alias configuracoes_xfce4='xfce4-settings-manager'
alias escanear_pc='fucking clamscan --recursive=yes --infected --exclude-dir="/(usr/share|proc|sys|dev|run|tmp|var/tmp|mnt|media)|/home/none/(\.cache|\.mozilla)|/home/ivone/(\.cache|\.mozilla)"  /'
alias ultimo_container='python3 ~/ferramentas_usuario/nome_ultimo_container.py'
alias rodar_imagem_docker='fucking docker run -it'
alias listar_todos_os_containers_dockers='fucking docker ps -a'
alias remover_todos_os_containers_parados='fucking docker container prune -f'
alias rodar_ultimo_container_ativo='fucking docker exec -it `ultimo_container` bash'
alias parar_ultimo_container='fucking docker stop `ultimo_container`'
alias remover_ultimo_container='fucking docker remove `ultimo_container`'
alias ativar_e_rodar_ultimo_container='ativar_e_rodar_container `ultimo_container` bash'
alias conectar_vpn='python3 ~/ferramentas_usuario/conectar_vpn.py'
alias desconectar_vpn='python3 ~/ferramentas_usuario/desconectar_vpn.py'
alias baixar_pasta_via_http='wget -r -np -nH --cut-dirs=3 -R index.html'
alias converter_imagem='convert -resize 200x200 -quality 72'
alias tarball_sem_compressao='tar -cvf'

# FUNÇÕES

procurar(){
find $2 -iname $1
}

arquivos_ocultos(){
find $1 -iname '.*' -type f
}

pastas_ocultas(){
find $1 -iname '.*' -type d
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

baixar_musica(){
yt-dlp -f 'ba' -x --audio-format mp3 --embed-thumbnail "$1" -o '%(title)s.mp3'
}

historico_programas_desinstalados(){
tail -n $1 /var/log/apt/history.log
}

remover_recursivamente(){
    find "$2" -name "$1" -exec rm -rf {} \; 2>/dev/null
}

atualizar_pywal() {
    if [ -e ~/.cache/wal/sequences ]
    then
        (cat ~/.cache/wal/sequences &);
        source ~/.cache/wal/colors-tty.sh
    else
        echo "Rode o comando wal -i /local/da/imagem.jpg"
    fi
}

criar_imagem_docker() {
    fucking docker build -t $1 . -f $2
}

ativar_e_rodar_container() {
    fucking docker start $1
    fucking docker exec -it $1 $2
}

remover_dados_exif() {
  convert $1 -strip $2
}

trocar_nomes() {
    if [ $# -ne 2 ]; then
        echo "Uso: trocar_nomes item1 item2"
        return 1
    fi

    item1="$1"
    item2="$2"

    # Criando um nome temporário para evitar conflitos
    temp_nome="temp_$RANDOM"

    # Renomeando os itens
    mv "$item1" "$temp_nome"
    mv "$item2" "$item1"
    mv "$temp_nome" "$item2"
}

# function dominio_comprado { whois "$1" 2>/dev/null | grep -q 'Registrant' && echo "comprado." || echo "disponível." }


# IMPORTAR CONFIGURAÇÕES EXCLUSIVAS DE CADA SISTEMA
if [ -f /etc/arch-release ]; then
  source ~/.bash_aliases_arch
elif [ -f /etc/debian_version ]; then
  source ~/.bash_aliases_debian
fi
