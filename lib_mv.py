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
  subprocess.run(['find', './', '-type', 'f', '-exec', 'sed', '-i', f's/Simple Bookstore App/GRUPO27/g', '{{}}', '\;'])
  os.chdir('practica_creativa2/bookinfo/src/productpage')
  subprocess.call(['pip3', 'install', '-r', 'requirements.txt'])
  subprocess.call(['python3', 'productpage_monolith.py', f'{puerto}'])

# Despliegue de la aplicación mediante Docker
def mv_docker ():
  log.debug("mv_docker ")
  subprocess.call(['sudo', 'docker', 'build', '-t', 'g27/product-page-mono', '.'])
  subprocess.call(['sudo', 'docker', 'run', '--name', 'g27-product-page-mono', '-p', '9080:9080', '-e', 'GROUP_NUMBER=27', 'g27/product-page-mono'])

# Eliminar todas las imágenes y contenedores Docker
def docker_destroy():
  subprocess.call(['sudo docker stop $(sudo docker ps -aq)'], shell=True)
  subprocess.call(['sudo docker rm $(sudo docker ps -aq)'], shell=True)
  subprocess.call(['sudo docker rmi --force $(sudo docker images -q)'], shell=True)

# Despliegue de la aplicación mediante Docker-Compose
def mv_docker_compose (version, ratings, star):
  log.debug("mv_docker_compose ")
  # Guardar directorio raíz
  raiz = os.getcwd()
  # Clonar repositorio de la app
  subprocess.call(['git', 'clone', 'https://github.com/CDPS-ETSIT/practica_creativa2.git', '/practica_creativa2'])
  # Crear la imagen de ProductPage
  log.debug("CONSTRUIR PRODUCT_PAGE")
  subprocess.call(['sudo', 'docker', 'build', '-t', 'g27/product-page:latest', './ProductPage'])
  subprocess.call(['sudo', 'docker', 'run', '--name', 'g27-product-page', '-p', '9080', '-d', '-it', 'g27/product-page:latest'])
  # Crear la imagen de Details
  log.debug("CONSTRUIR DETAILS")
  subprocess.call(['sudo', 'docker', 'build', '-t', 'g27/details:latest', './Details'])
  subprocess.call(['sudo', 'docker', 'run', '--name', 'g27-details', '-p', '9080', '-d', '-it', 'g27/details:latest'])
  # Crear la imagen de Ratings
  log.debug("CONSTRUIR RATINGS")
  subprocess.call(['sudo', 'docker', 'build', '-t', 'g27/ratings:latest', './Ratings'])
  subprocess.call(['sudo', 'docker', 'run', '--name', 'g27-ratings', '-p', '9080', '-d', '-it', 'g27/ratings:latest'])
  # Crear la imagen de Reviews
  log.debug("CONSTRUIR REVIEWS")
  os.chdir('practica_creativa2/bookinfo/src/reviews')
  subprocess.call(['sudo', 'docker', 'run', '--rm', '-u', 'root', '-v', '/home/gradle/project', '-w', '/home/gradle/project', 'gradle:4.8.1', 'gradle', 'clean', 'build'])
  subprocess.call(['sudo', 'docker', 'build', '-t', 'g27/reviews:latest', './reviews-wlpcfg'])
  subprocess.call(['sudo', 'docker', 'run', '--name', 'g27-reviews', '-p', '9080', '-d', '-it', 'g27/reviews:latest'])
  
  # Cambiar al directorio raíz
  os.chdir(raiz)
  # Crear el contenido del fichero docker-compose.yaml
  log.debug("CONSTRUIR DOCKER_COMPOSE")
  contenido_docker_compose = f"""
      version: '3'
      services:
        g27-productpage:
          image: "g27/product-page:latest"
          ports:
            - 9080:9080
          environment:
            - GROUP_NUMBER=27
        g27-details:
          image: "g27/details:latest"
          environment:
            - SERVICE_VERSION=v1
            - ENABLE_EXTERNAL_BOOK_SERVICE=true
        g27-reviews:
          image: "g27/reviews:latest"
          environment:
            - SERVICE_VERSION={version}
            - ENABLE_RATINGS={ratings}
            - STAR_COLOR={star}
        g27-ratings:
          image: "g27/ratings:latest"
      """
  # Escribir el contenido en el fichero docker-compose.yaml
  with open('docker-compose.yaml', 'w') as file:
    file.write(contenido_docker_compose)

  # Crear los contenedores
  #subprocess.call(['sudo', 'docker-compose', 'up', '-d'])
  #subprocess.call(['sudo', 'docker-compose', 'build'])
  subprocess.call(['sudo', 'docker-compose', 'up'])

def config_cluster(cluster):
  # Configurar el cluster
  subprocess.call(['gcloud', 'container', 'clusters', 'resize', f'{cluster}', '--num-nodes=5', '--zone=europe-southwest1'])
  subprocess.call(['gcloud', 'container', 'clusters', 'update', f'{cluster}', '--no-enable-autoscaling', '--zone=europe-southwest1'])
  subprocess.call(['gcloud', 'auth', 'configure-docker', '-q'])

def mv_kubernetes(version):
  log.debug("mv_kubernetes ")
  # Desplegar el escenario
  subprocess.call(['kubectl', 'apply', '-f', f'./deployment-{version}.yaml'])
  # Mostrar información de los pods y los services
  subprocess.call(['kubectl', 'get', 'pods'])
  subprocess.call(['kubectl', 'get', 'services'])

def destroy_cluster():
  # Destruir el escenario de la parte 4
  subprocess.call(['kubectl', 'delete', '--all', 'pods'])
  subprocess.call(['kubectl', 'delete', '--all', 'deployments'])
  subprocess.call(['kubectl', 'delete', '--all', 'services'])

def info_cluster():
  # Mostrar información de los pods y los services
  subprocess.call(['kubectl', 'get', 'pods'])
  subprocess.call(['kubectl', 'get', 'services'])