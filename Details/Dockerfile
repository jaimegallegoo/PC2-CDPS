FROM ruby:2.7.1-slim

# Actualizar sistema
RUN apt-get update -y

#Instalar github
RUN apt-get install -y git

# Clonar repositorio de la app
RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git /app

# Cambiar directorio al de details
WORKDIR /app/bookinfo/src/details

# Copiar el fichero details.rb
COPY details.rb /opt/microservices/

# Especificar variables de entorno
ENV SERVICE_VERSION v1
ENV ENABLE_EXTERNAL_BOOK_SERVICE true

# Indicar el puerto accesible
EXPOSE 9080

# Lanzar app en el puerto 9080
CMD ["ruby", "details.rb", "9080"]

# Indicar que se ha instalado correctamente
RUN echo "La imagen Docker se ha instalado correctamente"