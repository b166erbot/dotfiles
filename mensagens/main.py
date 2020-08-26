#!/usr/bin/python3
from src.ferramentas import main
from contextlib import suppress
from os import chdir
from pathlib import Path


if __name__ == '__main__':
    local_deste_arquivo = Path(__file__).parent
    chdir(local_deste_arquivo)
    with suppress(KeyboardInterrupt, EOFError):
        main()
    print('\nprograma finalizado')
