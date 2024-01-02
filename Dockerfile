FROM ubuntu:18.04

#Instalar apache
RUN apt-get update -y
RUN apt-get install -y apache2

#Indicar el puerto accesible
EXPOSE 9080

#Indicar que se ha instalado correctamente
CMD echo "La imagen Docker se ha instalado correctamente"