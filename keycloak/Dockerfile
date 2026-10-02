# лучше использовать FROM quay.io/keycloak/keycloak:latest AS builder,
# в нем удалено все лишнее для безопасности

FROM debian:13

ENV DEBIAN_FRONTEND=noninteractive

# Устанавливаем зависимости
RUN apt-get update && apt-get install -y --no-install-recommends \
    gnupg \
    curl \
    ca-certificates \
    openjdk-25-jre \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Создаем рабочую директорию
WORKDIR /kc

RUN wget -qO- https://github.com/keycloak/keycloak/releases/download/26.7.4/keycloak-26.7.4.tar.gz | tar -xz --strip-components=1

RUN openssl req -x509 -newkey rsa:4096 -nodes \
  -keyout /kc/conf/server.key.pem \
  -out /kc/conf/server.crt.pem \
  -days 3650 \
  -subj "/CN=keycloak" \
  -addext "subjectAltName=DNS:keycloak"

COPY keycloak.conf /kc/conf

# здесь в шаге build можно подобавлять опции специфичные для окружения
RUN /kc/bin/kc.sh build

# для безопасности лучше сделать новый билд и скопировать туда папку /kc
# чтоб не оставлять в образе установленные зависимости на apt install шаге
