FROM python:3.6.9

# Indicar el puerto accesible
EXPOSE 9080

# Cambiar directorio al de productpage
WORKDIR /home

# Actualizar sistema
RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2 \
    && apt-get update \
    && apt-get install -y python3-pip \
    && pip install --upgrade pip \
    && apt-get install -y git \
    && pip3 install -r practica_creativa2/bookinfo/src/productpage/requirements.txt

# Lanzar app en el puerto 9080
CMD ["python3", "practica_creativa2/bookinfo/src/productpage/productpage.py", "9080"]

# Indicar que se ha instalado correctamente
RUN echo "La imagen Docker se ha instalado correctamente"