from os import system as sy
from pathlib import Path


def main():
    local = Path(__file__).parent

    # backup pacotes atom
    # sy(f"apm list --installed --bare > {local}/atom.pacotes")


if __name__ == '__main__':
    main()
