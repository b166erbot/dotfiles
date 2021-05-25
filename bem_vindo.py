# dotfiles: https://www.atlassian.com/git/tutorials/dotfiles

from time import sleep
from random import choice
from os import get_terminal_size
from colored import fg, bg, attr


# def cortar(texto, numero):
#     return [texto[x: x+numero] for x in range(0, len(texto), numero)]


def cortar2(texto, numero):
    texto2 = texto.split()
    temp = []
    texto_cortado = []
    while bool(texto2):
        while len(' '.join(temp)) < numero and bool(texto2):
            temp.append(texto2.pop(0))
        if len(' '.join(temp)) > numero:
            texto2.insert(0, temp.pop())
        texto_cortado.append(' '.join(temp))
        temp = []
    return texto_cortado


# def texto_efeito_pausa(texto: str):
#     for letra in texto:
#         print(letra, end='', flush=True)
#         sleep(0.07)
#     print()


def main():
    cores = [
        'red', 'green', 'yellow', 'blue', 'cyan', 'dark_gray',
        'light_red', 'light_green', 'light_yellow', 'light_blue', 'light_cyan'
    ]
    textos = [
        'fuck society', 'free your mind', 'hello friend', 'bazinga!',
        'may the force be with you', 'follow the white habbit',
        'One Ring to rule them all, One Ring to find them, One Ring '
        'to bring them all, And in the darkness bind them',
        'I solemnly swear that I am up to no good',
        'the gravity can cross the dimensions, including time',
        'stay'
    ]
    # texto_efeito_pausa(choice(textos))
    texto = choice(textos)
    tamanho_tela = get_terminal_size()[0]
    texto_cortado = cortar2(texto, tamanho_tela - 4)
    cor = choice(cores)
    print(fg(cor) + bg('black'))
    for texto in texto_cortado:
        texto = f"| {texto} |"
        barra = '-' * len(texto)
        print(barra.center(tamanho_tela))
        print(texto.center(tamanho_tela))
        print(barra.center(tamanho_tela))
    print(attr(0))


if __name__ == '__main__':
    main()
