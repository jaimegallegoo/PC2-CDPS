FROM python:3.7.7-slim

# Indicar el puerto accesible
EXPOSE 9080

# Cambiar directorio al de home
WORKDIR /home

# Actualizar sistema e instalar dependencias
RUN apt-get update \
    && apt-get install -y git \
    && git clone https://github.com/CDPS-ETSIT/practica_creativa2.git /practica_creativa2 \
    && apt-get install -y python3-pip \
    && pip3 install -r practica_creativa2/bookinfo/src/productpage/requirements.txt

# Cambiar directorio al de productpage
WORKDIR /practica_creativa2/bookinfo/src/productpage/

# Lanzar app en el puerto 9080
CMD ["python3", "productpage.py", "9080"]

# Indicar que se ha instalado correctamente
RUN echo "La imagen Docker de PRODUCT PAGE se ha instalado correctamente"