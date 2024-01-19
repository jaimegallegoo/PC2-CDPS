FROM debian:10

# Indicar el puerto accesible
EXPOSE 9080

# Indicar la variable de entorno
ENV GROUP_NUMBER=UNDEFINED

# Cambiar directorio al de practica_creativa2
WORKDIR /home

# Instalar dependencias
RUN apt-get update -y \
    && apt-get install -y python3-pip git \
    && git clone https://github.com/CDPS-ETSIT/practica_creativa2.git \
    && cd practica_creativa2/bookinfo/src/productpage/ \
    && pip3 install -r requirements.txt

# Cambiar el título de la app y lanzar app en el puerto 9080
RUN grep -rl "Simple Bookstore App" ./ | xargs awk -i inplace '{gsub(/Simple Bookstore App/, "Simple Bookstore App($GROUP_NUMBER)")}1' \
    && python3 practica_creativa2/bookinfo/src/productpage/productpage_monolith.py 9080

# Indicar que se ha instalado correctamente
RUN echo "La imagen Docker se ha instalado correctamente"