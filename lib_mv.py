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
def mv_docker_compose (version, ratings, star):
  log.debug("mv_docker_compose ")
  #Guardar directorio raíz
  raiz = os.getcwd()
  #Clonar repositorio de la app
  subprocess.call(['git', 'clone', 'https://github.com/CDPS-ETSIT/practica_creativa2.git'])
  #Crear la imagen de ProductPage
  log.debug("CONSTRUIR PRODUCT_PAGE")
  subprocess.call(['sudo', 'docker', 'build', '-t', 'g27/product-page', './ProductPage'])
  #Crear la imagen de Details
  log.debug("CONSTRUIR DETAILS")
  subprocess.call(['sudo', 'docker', 'build', '-t', 'g27/details', './Details'])
  #Crear la imagen de Reviews
  log.debug("CONSTRUIR REVIEWS")
  os.chdir('practica_creativa2/bookinfo/src/reviews/')
  #subprocess.call(['sudo', 'docker', 'run', '--rm', '-u', 'root', '-v', f'{raiz}:/home/gradle/project', '-w', '/home/gradle/project', 'gradle:4.8.1', 'gradle', 'clean', 'build'])
  subprocess.call(['sudo', 'docker', 'build', '--build-arg', 'service_version=v1', '--build-arg', 'enable_ratings=false', '-t', 'g27/reviews-v1', './reviews-wlpcfg'])
  subprocess.call(['sudo', 'docker', 'build', '--build-arg', 'service_version=v2', '--build-arg', 'enable_ratings=true', '--build-arg', 'star_color=black', '-t', 'g27/reviews-v2', './reviews-wlpcfg'])
  subprocess.call(['sudo', 'docker', 'build', '--build-arg', 'service_version=v3', '--build-arg', 'enable_ratings=true', '--build-arg', 'star_color=red', '-t', 'g27/reviews-v3', './reviews-wlpcfg'])
  
  #Cambiar al directorio raíz
  os.chdir(raiz)
  #Crear la imagen de Ratings
  log.debug("CONSTRUIR RATINGS")
  subprocess.call(['sudo', 'docker', 'build', '-t', 'g27/ratings', './Ratings'])

  #Crear el contenido del fichero docker-compose.yaml
  log.debug("CONSTRUIR DOCKER_COMPOSE")
  contenido_docker_compose = f"""
      version: '3.3'

      services:
        g27-productpage:
          image: g27/product-page
          ports:
            - "9080"

        g27-details:
          image: g27/details
          ports:
            - "9080"

        g27-reviews:
          image: g27/reviews-{version}
          ports:
            - "9080"
          environment:
            - SERVICE_VERSION={version}
            - ENABLE_RATINGS={ratings}
            - STAR_COLOR={star}

        g27-ratings:
          image: g27/ratings
          ports:
            - "9080"
      """
  #Escribir el contenido en el fichero docker-compose.yaml
  with open('docker-compose.yaml', 'w') as file:
    file.write(contenido_docker_compose)

  #Crear los contenedores
  subprocess.call(['sudo', 'docker-compose', 'up', '-d'])
  #subprocess.call(['sudo', 'docker-compose', '--env-file', 'envs_v1.env', 'up'])
  #subprocess.call(['sudo', 'docker-compose', 'up', '--build'])