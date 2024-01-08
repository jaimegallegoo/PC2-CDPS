FROM ruby:2.7.1-slim

# Indicar el puerto accesible
EXPOSE 9080

# Cambiar directorio al de home
WORKDIR /home

# Especificar variables de entorno
ENV SERVICE_VERSION v1
ENV ENABLE_EXTERNAL_BOOK_SERVICE true

# Actualizar sistema e instalar dependencias
RUN apt-get update \
    && apt-get install -y git \
    && git clone https://github.com/CDPS-ETSIT/practica_creativa2.git /practica_creativa2

WORKDIR /practica_creativa2/bookinfo/src/details

RUN cp details.rb /opt/microservices/

# Cambiar directorio al de details
WORKDIR /opt/microservices

# Lanzar app en el puerto 9080
CMD ["ruby", "details.rb", "9080"]

# Indicar que se ha instalado correctamente
RUN echo "La imagen Docker de DETAILS se ha instalado correctamente"