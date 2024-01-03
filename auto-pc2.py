# GRUPO 27
# Jaime Gallego Chillón
# Marta Volpini López

import logging, sys, os
from lib_mv import mv_pesada, mv_docker, mv_docker_compose

def init_log():
    # Creacion y configuracion del logger
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger('auto_p2')
    ch = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', "%Y-%m-%d %H:%M:%S")
    ch.setFormatter(formatter)
    log.addHandler(ch)
    log.propagate = False

def pause():
    programPause = input("Press the <ENTER> key to continue...")

def main():

    # Establecer la posición de la orden en la línea de argumentos
    orden = sys.argv[1]

    if orden == "parte1":
        puerto = sys.argv[2]
        mv_pesada(puerto)

    elif orden == "parte2":
        mv_docker()

    elif orden == "parte3":
        version = sys.argv[2]
        if version == "v1":
            mv_docker_compose("v1", False, "black")
        elif version == "v2":
            mv_docker_compose("v2", True, "black")
        else:
            mv_docker_compose("v3", True, "red")

    else:
        print(f"Orden no reconocida: {orden}")

if __name__ == "__main__":
    main()