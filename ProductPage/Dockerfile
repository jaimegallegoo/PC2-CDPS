FROM python:3.7.7-slim

# Indicar el puerto accesible
EXPOSE 9080

# Cambiar directorio al de productpage
WORKDIR /home

# Actualizar sistema
RUN apt-get update
RUN apt-get install -y python3-pip

# Instalar git
RUN apt-get install -y git

# Clonar repositorio de la app
RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git

RUN cd practica_creativa2/bookinfo/src/productpage/

# Instalar requerimientos
RUN pip3 install -r requirements.txt

# Lanzar app en el puerto 9080
CMD ["python3", "practica_creativa2/bookinfo/src/productpage/productpage.py", "9080"]

# Indicar que se ha instalado correctamente
RUN echo "La imagen Docker se ha instalado correctamente"