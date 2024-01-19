# GRUPO 27
# Jaime Gallego Chillón
# Marta Volpini López

import logging, sys, os
from lib_mv import mv_pesada, mv_docker, mv_docker_compose, mv_kubernetes, destroy_cluster, config_cluster, docker_destroy

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
    #python3 auto-pc2.py parte1 9080

    elif orden == "parte2":
        if sys.argv[2] != "destruir":
           mv_docker()
        else:
            docker_destroy()
    #python3 auto-pc2.py parte2

    elif orden == "parte3":
        version = sys.argv[2]
        if version == "v1":
            mv_docker_compose("v1", False, "black")
        elif version == "v2":
            mv_docker_compose("v2", True, "black")
        else:
            mv_docker_compose("v3", True, "red")
    #python3 auto-pc2.py parte3 v1
    #python3 auto-pc2.py parte3 v2
    #python3 auto-pc2.py parte3 v3

    elif orden == "parte4":
        if sys.argv[2] != "destruir":
            cluster = sys.argv[2]
            if sys.argv[3] == "configurar":
                config_cluster(cluster)
            else:
                version = sys.argv[3]
                mv_kubernetes(version)
        else:
            destroy_cluster()
    #python3 auto-pc2.py parte4 nombre-cluster configurar
    #python3 auto-pc2.py parte4 nombre-cluster v1     
    #python3 auto-pc2.py parte4 nombre-cluster v2
    #python3 auto-pc2.py parte4 nombre-cluster v3 
    #python3 auto-pc2.py parte4 destruir

    else:
        print(f"Orden no reconocida: {orden}")

if __name__ == "__main__":
    main()