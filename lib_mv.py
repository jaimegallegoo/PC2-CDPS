#!/usr/bin/python3

# GRUPO 27
# Jaime Gallego Chillón
# Marta Volpini López

import logging, subprocess

log = logging.getLogger('auto_p2')

# Despliegue de la aplicación en máquina virtual pesada
def mv_pesada (puerto):
  log.debug("mv_pesada ")
  subprocess.call(['git', 'clone', 'https://github.com/CDPS-ETSIT/practica_creativa2.git'])
  subprocess.call(['cd', 'practica_creativa2/bookinfo/src/productpage'])
  subprocess.call(['pip3', 'install', '-r', 'requirements.txt'])
  subprocess.call(['python3', 'productpage_monolith.py', f'{puerto}'])