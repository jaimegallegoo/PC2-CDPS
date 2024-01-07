FROM ruby:2.7.1-slim

# Indicar el puerto accesible
EXPOSE 9080

# Cambiar directorio al de home
WORKDIR /home

# Actualizar sistema e instalar dependencias
RUN apt-get update \
    && apt-get install -y git \
    && git clone https://github.com/CDPS-ETSIT/practica_creativa2.git

# Especificar variables de entorno
ENV SERVICE_VERSION v1
ENV ENABLE_EXTERNAL_BOOK_SERVICE true

# Copiar el fichero details.rb en la ruta /opt/microservices/
COPY practica_creativa2/bookinfo/src/details/details.rb /opt/microservices/

# Lanzar app en el puerto 9080
CMD ["ruby", "practica_creativa2/bookinfo/src/details/details.rb", "9080"]

# Indicar que se ha instalado correctamente
RUN echo "La imagen Docker se ha instalado correctamente"