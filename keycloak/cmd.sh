#!/bin/bash

set -e

# Функция для сборки контейнеров
build() {
    echo "Сборка контейнеров..."
    docker compose -f docker-compose.yml build
}

# Функция для старта контейнеров
start() {
    echo "Запуск контейнеров..."
    docker compose -f docker-compose.yml up -d
    echo "После инициализации keycloak - открыть в браузере https://keycloak:8443/admin"
}

# Функция для остановки контейнеров
stop() {
    if [ "$1" = "-v" ]; then
        echo "Остановка и удаление контейнеров (включая volumes)..."
        docker compose -f docker-compose.yml down -v --timeout 0
    else
        echo "Остановка и удаление контейнеров..."
        docker compose -f docker-compose.yml stop --timeout 0
    fi
}

dev() {
    docker compose exec -it keycloak-dev bash
}

# Обработка переданного аргумента
case "$1" in
    build)
        build
        ;;
    start)
        start
        ;;
    stop)
        stop
        ;;
    test)
        test
        ;;
    dev)
        dev
        ;;
    *)
        echo "Использование: $0 {build|start|stop|dev}"
        exit 1
        ;;
esac
