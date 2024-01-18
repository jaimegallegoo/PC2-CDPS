FROM debian:10

# Indicar el puerto accesible
EXPOSE 9080

#Indicar la variable de entorno
ENV GROUP_NUMBER=UNDEFINED

# Cambiar directorio al de practica_creativa2
WORKDIR /home

# Actualizar sistema
RUN apt-get update -y

#Instalar pip
RUN apt-get install -y python3-pip

#Instalar github
RUN apt-get install -y git

# Clonar repositorio de la app
RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git /practica_creativa2

# Cambiar directorio al de productpage
WORKDIR /practica_creativa2/bookinfo/src/productpage

# Instalar requerimientos
RUN pip3 install -r requirements.txt

# Cambiar directorio al de practica_creativa2
WORKDIR /home

# Cambiar el título de la app y lanzar app en el puerto 9080
CMD find ./ -type f -exec sed -i "s/Simple Bookstore App/Simple Bookstore App($GROUP_NUMBER)/g" {} \; \
    && python3 practica_creativa2/bookinfo/src/productpage/productpage_monolith.py 9080

# Indicar que se ha instalado correctamente
RUN echo "La imagen Docker se ha instalado correctamente"