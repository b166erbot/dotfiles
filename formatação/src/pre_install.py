from os import getuid


try:
    from .fazer_backup import fazer_backup
except ImportError:
    from fazer_backup import fazer_backup


def root() -> bool:
    return getuid() == 0


def pre_install(argumentos):
    if root():
        print('o pre_install seria melhor ser executado com o usuário comum')
        exit(1)

    fazer_backup(argumentos)
    print('agora, alguns lembretes:')
    print('fazer backup dos arquivos da mãe!')
