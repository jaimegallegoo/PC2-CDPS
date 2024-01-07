FROM node:14-slim

# Indicar el puerto accesible
EXPOSE 9080

# Cambiar directorio al de home
WORKDIR /opt/microservices

# Actualizar sistema e instalar dependencias
RUN apt-get update && apt-get install -y git \
    && git clone https://github.com/CDPS-ETSIT/practica_creativa2.git \
    && cp practica_creativa2/bookinfo/src/ratings/package.json /opt/microservices \
    && cp practica_creativa2/bookinfo/src/ratings/ratings.js /opt/microservices \
    && npm install

# Cambiar directorio al de details
# WORKDIR /opt/microservices

# Lanzar app en el puerto 9080
CMD ["node", "ratings.js", "9080"]

# Indicar que se ha instalado correctamente
RUN echo "La imagen Docker de RATINGS se ha instalado correctamente"
