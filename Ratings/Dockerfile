FROM node:12.18.1-slim

# Indicar el puerto accesible
EXPOSE 9080

# Crear directorio de trabajo
WORKDIR /opt/microservices

# Actualizar sistema e instalar dependencias
RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && git clone https://github.com/CDPS-ETSIT/practica_creativa2.git \
    && cp practica_creativa2/bookinfo/src/ratings/package.json /opt/microservices \
    && cp practica_creativa2/bookinfo/src/ratings/ratings.js /opt/microservices \
    && npm install \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Lanzar app en el puerto 9080
CMD ["node", "ratings.js", "9080"]

# Indicar que se ha instalado correctamente
RUN echo "La imagen Docker se ha instalado correctamente"
