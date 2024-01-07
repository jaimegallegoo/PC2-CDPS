FROM ruby:2.7.1-slim

# Indicar el puerto accesible
EXPOSE 9080

# Cambiar al directorio /opt/microservices
WORKDIR /opt/microservices

# Especificar variables de entorno
ENV SERVICE_VERSION v1
ENV ENABLE_EXTERNAL_BOOK_SERVICE true

# Copiar el fichero details.rb en la ruta /opt/microservices/
COPY practica_creativa2/bookinfo/src/details/details.rb .

# Lanzar app en el puerto 9080
CMD ["ruby", "details.rb", "9080"]

# Indicar que se ha instalado correctamente
RUN echo "La imagen Docker se ha instalado correctamente"