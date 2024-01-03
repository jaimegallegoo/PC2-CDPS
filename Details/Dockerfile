# Utilizar la imagen base de Ruby 2.7.1 slim
FROM ruby:2.7.1-slim

# Instalar Git (necesario para clonar el repositorio)
RUN apt-get update && apt-get install -y git

# Clonar el repositorio
RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git /opt/microservices

# Establecer el directorio de trabajo
WORKDIR /opt/microservices/bookinfo/src/details

# Copiar el fichero details.rb en la ruta /opt/microservices/ dentro del contenedor
COPY details.rb .

# Especificar variables de entorno
ENV SERVICE_VERSION v1
ENV ENABLE_EXTERNAL_BOOK_SERVICE true

# Exponer el puerto 9080
EXPOSE 9080

# Ejecutar el fichero details.rb usando la instrucción ruby y añadir el puerto
CMD ["ruby", "details.rb", "9080"]