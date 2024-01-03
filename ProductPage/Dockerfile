FROM python:3.7-alpine

# Actualizar sistema
RUN apk update && apk upgrade

# Instalar git
RUN apk add git

# Clonar repositorio de la app
RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git

# Cambiar directorio al de productpage
WORKDIR /practica_creativa2/bookinfo/src/productpage

# Instalar requerimientos
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Indicar el puerto accesible
EXPOSE 9080

# Lanzar app en el puerto 9080
CMD ["python3", "productpage.py", "9080"]

# Indicar que se ha instalado correctamente
RUN echo "La imagen Docker se ha instalado correctamente"