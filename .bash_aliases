# ALIASES

alias config='git --git-dir=/home/none/.cfg/ --work-tree=/home/none' # git dotfiles
alias portas-abertas='ss -atunpl'
alias ips='ip -c -br a'
alias ver-tamanho='du -sh'
alias tempo-de-inicializacao-dos-programas='systemd-analyze blame'
alias git-parar-tracking='config rm --cached -r'
alias fucking='sudo'
alias abrir='exo-open'
alias variaveis='set'
alias meu-ip='ip route get 1 | awk "{print \$7}"'
alias editar-alias='nano ~/.bash_aliases'
alias editar-alias-debian='nano ~/.bash_aliases_debian'
alias editar-alias-arch='nano ~/.bash_aliases_arch'
alias ver-processador='inxi -bGI'
alias ver-processos='ps aux'
alias help='run-help'
alias montar-e-transferir-musicas='python3 ~/python\ scripts/scripts/montar_celular_e_transferir_musicas.py'
alias contar-arquivos-pastas='echo "$(ls -a | wc -l) - 2" | bc'
alias ver-atalhos='scripts ver-atalhos'
alias git-ver-rastreados='config ls-tree -r master --name-only'
alias montar-celular='python3 ~/python\ scripts/scripts/_montar_celular.py --ip 3'
alias substituir='mv -f'
alias chat='shell-genie ask'
alias mover-e-alterar-dono='fucking `which scripts` mover-e-alterar-dono'
alias ver-arquitetura-pro='uname -m'
alias atualizar-shell='source ~/.zshrc'
alias remover-exif='mogrify -strip'
alias trocar-usuario='dm-tool switch-to-greeter'
alias configuracoes-xfce4='xfce4-settings-manager'
alias escanear-pc='fucking clamscan --recursive=yes --infected --exclude-dir="/(usr/share|proc|sys|dev|run|tmp|var/tmp|mnt|media)|/home/none/(\.cache|\.mozilla)|/home/ivone/(\.cache|\.mozilla)"  /'
alias ultimo-container='python3 ~/ferramentas_usuario/nome_ultimo_container.py'
alias rodar-imagem-docker='fucking docker run -it'
alias listar-todos-os-containers-dockers='fucking docker ps -a'
alias remover-todos-os-containers-parados='fucking docker container prune -f'
alias rodar-ultimo-container-ativo='fucking docker exec -it `ultimo-container` bash'
alias parar-ultimo-container='fucking docker stop `ultimo-container`'
alias remover-ultimo-container='fucking docker remove `ultimo-container`'
alias ativar-e-rodar-ultimo-container='ativar-e-rodar-container `ultimo-container` bash'
alias conectar-vpn='python3 ~/ferramentas_usuario/conectar_vpn.py'
alias desconectar-vpn='python3 ~/ferramentas_usuario/desconectar_vpn.py'
alias baixar-pasta-via-http='wget -r -np -nH --cut-dirs=3 -R index.html'
alias converter-imagem='convert -resize 200x200 -quality 72'
alias tarball-sem-compressao='tar -cvf'
alias atualizar-sistema='fucking do-release-upgrade'

# FUNÇÕES

procurar(){
find $2 -iname $1
}

arquivos-ocultos(){
find $1 -iname '.*' -type f
}

pastas-ocultas(){
find $1 -iname '.*' -type d
}

pastas-vazias(){
find $1 -type d -empty
}

arquivos-vazios(){
find $1 -type f -empty
}

arquivos-executaveis(){
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

baixar-musica(){
yt-dlp -f 'ba' -x --audio-format mp3 --embed-thumbnail "$1" -o '%(title)s.mp3'
}

historico-programas-desinstalados(){
tail -n $1 /var/log/apt/history.log
}

remover-recursivamente(){
    find "$2" -name "$1" -exec rm -rf {} \; 2>/dev/null
}

atualizar-pywal() {
    if [ -e ~/.cache/wal/sequences ]
    then
        (cat ~/.cache/wal/sequences &);
        source ~/.cache/wal/colors-tty.sh
    else
        echo "Rode o comando wal -i /local/da/imagem.jpg"
    fi
}

criar-imagem-docker() {
    fucking docker build -t $1 . -f $2
}

ativar-e-rodar-container() {
    fucking docker start $1
    fucking docker exec -it $1 $2
}

remover-dados-exif() {
  convert $1 -strip $2
}

trocar-nomes() {
    if [ $# -ne 2 ]; then
        echo "Uso: trocar-nomes item1 item2"
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
