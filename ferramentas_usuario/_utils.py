import os


def está_instalado(programa: str) -> bool:
    """Verifica se o programa está instalado no pc."""
    for local in os.environ["PATH"].split(os.pathsep):
        try:
            if programa in os.listdir(local):
                return True
        except FileNotFoundError:
            pass
    return False