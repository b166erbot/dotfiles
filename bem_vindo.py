from time import sleep
from random import choice


def texto_efeito_pausa(texto: str):
    for letra in texto:
        print(letra, end='', flush=True)
        sleep(0.07)
    print()


def main():
    textos = [
        'fuck society', 'free your mind', 'hello friend'
    ]
    texto_efeito_pausa(choice(textos))
    print()


if __name__ == '__main__':
    main()
