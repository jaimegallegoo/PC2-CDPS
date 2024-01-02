#!/usr/bin/python3

# GRUPO 27
# Jaime Gallego Chillón
# Marta Volpini López

import logging, subprocess, os

log = logging.getLogger('auto_p2')

# Despliegue de la aplicación en máquina virtual pesada
def mv_pesada (puerto):
  log.debug("mv_pesada ")
  subprocess.call(['git', 'clone', 'https://github.com/CDPS-ETSIT/practica_creativa2.git'])
  os.chdir('practica_creativa2/bookinfo/src/productpage')
  subprocess.call(['pip3', 'install', '-r', 'requirements.txt'])
  subprocess.call(['python3', 'productpage_monolith.py', f'{puerto}'])

# Despliegue de la aplicación mediante Docker
def mv_docker ():
  log.debug("mv_docker ")
  subprocess.call(['sudo', 'docker', 'build', '-t', 'g27/product-page', '.'])
  subprocess.call(['sudo', 'docker', 'run', '--name', 'g27-product-page', '-p', '9080:9080', '-d', 'g27/product-page'])

# Despliegue de la aplicación mediante Docker-Compose
def mv_docker_compose (version):
  log.debug("mv_docker_compose ")
  subprocess.call(['sudo', 'docker', 'build', '-t', 'g27/product-page', '/ProductPage'])
  subprocess.call(['sudo', 'docker', 'build', '-t', 'g27/details', '/Details'])
  #V1 subprocess.call(['sudo', 'docker', 'build', '--build-arg service_version=v1', '--build-arg enable_ratings=false', '-t', 'g27/reviews-v1', '/Reviews'])
  #V2 subprocess.call(['sudo', 'docker', 'build', '--build-arg service_version=v2', '--build-arg enable_ratings=true', '--build-arg star_color=black', '-t', 'g27/reviews-v2', '/Reviews'])
  #V3 subprocess.call(['sudo', 'docker', 'build', '--build-arg service_version=v3', '--build-arg enable_ratings=true', '--build-arg star_color=red', '-t', 'g27/reviews-v3', '/Reviews'])
  subprocess.call(['sudo', 'docker', 'build', '-t', 'g27/ratings', '/Ratings'])