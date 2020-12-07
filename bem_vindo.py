# dotfiles: https://www.atlassian.com/git/tutorials/dotfiles

from time import sleep
from random import choice
from os import get_terminal_size


# def texto_efeito_pausa(texto: str):
#     for letra in texto:
#         print(letra, end='', flush=True)
#         sleep(0.07)
#     print()


def main():
    textos = [
        'fuck society', 'free your mind', 'hello friend', 'bazinga!',
        'may the force be with you', 'follow the white habbit'
    ]
    # texto_efeito_pausa(choice(textos))
    tamanho_tela = get_terminal_size()[0]
    texto = f"| {choice(textos)} |"
    barra = '-' * len(texto)
    print(barra.center(tamanho_tela))
    print(texto.center(tamanho_tela))
    print(barra.center(tamanho_tela))
    print()


if __name__ == '__main__':
    main()
