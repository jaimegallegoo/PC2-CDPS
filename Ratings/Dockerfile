FROM node:12.18.1-slim

# Actualizar sistema
#RUN apt-get update -y

#Instalar github
#RUN apt-get install -y git

# Clonar repositorio de la app
RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git 

# Cambiar directorio al de ratings
WORKDIR /practica_creativa2/bookinfo/src/ratings

# Copiar los ficheros package.json y ratings.js
COPY package.json /opt/microservices/
COPY ratings.js /opt/microservices/

# Especificar variables de entorno
ENV SERVICE_VERSION v1

# Instalar las dependencias
RUN npm install

# Indicar el puerto accesible
EXPOSE 9080

# Lanzar app en el puerto 9080
CMD ["node", "ratings.js", "9080"]

# Indicar que se ha instalado correctamente
RUN echo "La imagen Docker se ha instalado correctamente"