FROM python:3.6.9
EXPOSE 9080
ENV GROUP_NUMBER=UNDEFINED
WORKDIR /home
RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2 \
        && apt-get update \
        && apt-get install -y python3-pip \
        && cd practica_creativa2/bookinfo/src/productpage/ \
        && pip3 install -r requirements.txt
CMD find ./ -type f -exec sed -i "s/Simple Bookstore App/Simple Bookstore App($GROUP_NUMBER)/g" {} \; \
  && python3 practica_creativa2/bookinfo/src/productpage/productpage_monolith.py 9080
