# antigo PS1 -> \[\e]0;\u@\h: \w\a\]${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$

PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\W\[\033[00m\]\$ '

# PATH
# comandos locais
export PATH=$PATH:/home/none/.local/bin
# /sbin
export PATH=$PATH:/sbin
# snap bin
export PATH=$PATH:/snap/bin
# /usr/bin/snap
export PATH=$PATH:/usr/bin/snap
# auto-complete para python3
export PYTHONSTARTUP=/home/none/.pythonrc

# ALIASES
alias config='/usr/bin/git --git-dir=/home/none/.cfg/ --work-tree=/home/none' # git dotfiles
