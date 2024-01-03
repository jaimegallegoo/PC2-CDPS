#FROM python:3.7-alpine
FROM debian:10

# Actualizar sistema
#RUN apk update && apk upgrade

# Instalar git
#RUN apk add git


# Actualizar sistema
RUN apt-get update -y

#Instalar pip
RUN apt-get install -y python3-pip

#Instalar github
RUN apt-get install -y git



# Clonar repositorio de la app
RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git

# Cambiar directorio al de productpage
WORKDIR /practica_creativa2/bookinfo/src/productpage

# Instalar requerimientos
#RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

# Indicar el puerto accesible
EXPOSE 9080

# Lanzar app en el puerto 9080
CMD ["python3", "productpage.py", "9080"]

# Indicar que se ha instalado correctamente
RUN echo "La imagen Docker se ha instalado correctamente"