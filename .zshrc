# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH="/home/none/.oh-my-zsh"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
# ZSH_THEME="robbyrussell"
# temas que eu gostei: bira, arrow, af-magic, fino-time
ZSH_THEME="af-magic"

# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
# a theme from this variable instead of looking in $ZSH/themes/
# If set to an empty array, this variable will have no effect.
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to automatically update without prompting.
DISABLE_UPDATE_PROMPT="true"

# Uncomment the following line to change how often to auto-update (in days).
export UPDATE_ZSH_DAYS=30

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS="true"

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# Caution: this setting can cause issues with multiline prompts (zsh 5.7.1 and newer seem to work)
# See https://github.com/ohmyzsh/ohmyzsh/issues/5765
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
# plugins=()

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"

# path
export PATH=$PATH:$HOME/.local/bin:$HOME/anaconda3/bin:/usr/local/bin

# sources
source $ZSH/oh-my-zsh.sh
source ~/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source ~/meu_token.sh
# colocando o comando conda no zsh
# source ~/anaconda3/etc/profile.d/conda.sh
# Comunicado: eu movi os aliases para o arquivo .bash_aliases
source ~/.bash_aliases

# COMPLETAÇÃO AUTOMATICA PARA SCRIPTS MEUS.
# scripts python instalados pelo setuptools (setup.py)
# por padrão você precisa criar para todos os scripts com o click uma
# variável assim: _(NOME_DO_SCRIPT)_COMPLETE
# eval "$(_SCRIPTS_COMPLETE=zsh_source scripts)"

# executáveis "compilados" pelo pyinstaller junto com a lib
# python3-argcomplete
# eval "$(register-python-argcomplete --shell zsh scripts)"


# colocando a cor do terminal com pywal
# primeiro rode wal -i /local/da/imagem.jpg
if [ -e ~/.cache/wal/sequences ]
then
  (cat ~/.cache/wal/sequences &);
  source ~/.cache/wal/colors-tty.sh
else
  echo rode o comando wal -i /local/da/imagem.jpg
fi

bem_vindo

# só use esses comandos abaixo caso tu use uma função com nome diferente
# do padrão (preexec)
# autoload -Uz add-zsh-hook
# add-zsh-hook preexec chupa_mundo

# Função chamada antes de adicionar o comando ao histórico
# zshaddhistory() {
#     # Obtém o comando atual que será executado
#     local comando="${1}"

#     # Execute o comando2 antes do comando digitado
#     executar_antes "$comando"

#     # Adicione o comando ao histórico
#     emulate -L zsh
#     fc -p "$comando"

#     # Execute o comando3 após a execução do comando
#     # comando3 "$comando"
# }

# Variável global para armazenar o tempo de início de cada comando
typeset -g _tempo_inicial_comandos

# Função que será executada antes de cada comando
preexec() {
    # Registra o tempo de início do comando
    _tempo_inicial_comandos=$(date +%s.%N)
}

# Função que será executada após a execução de cada comando
precmd() {
    if [[ -n "$_tempo_inicial_comandos" ]]; then
        # Calcula o tempo de execução do comando
        local _tempo_final_comandos=$(date +%s.%N)
        local _tempo_final=$(
          echo "$_tempo_final_comandos - $_tempo_inicial_comandos" | bc
        )

        # Exibe o tempo de execução na tela
        echo "Tempo de execução: ${_tempo_final} segundos"

        # Limpa o tempo de início para o próximo comando
        _tempo_inicial_comandos=""
    fi
}
