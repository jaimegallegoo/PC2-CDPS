FROM ruby:2.7.1-slim
EXPOSE 9080

WORKDIR /opt/microservices

ENV SERVICE_VERSION=v1
ENV ENABLE_EXTERNAL_BOOK_SERVICE=true

COPY practica_creativa2/bookinfo/src/details/details.rb /opt/microservices/

CMD ruby details.rb 9080