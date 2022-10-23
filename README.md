# devops-netology_ti_lisitsyn
Netology tasks, owner is TI_Lisitsyn
Files to ignore:
./idea
./terraform/test

Сценарий выполения задачи:

    создайте свой репозиторий на https://hub.docker.com;
    выберете любой образ, который содержит веб-сервер Nginx;
    создайте свой fork образа;
    реализуйте функциональность: запуск веб-сервера в фоне с индекс-страницей, содержащей HTML-код ниже:

<html>
<head>
Hey, Netology
</head>
<body>
<h1>I’m DevOps Engineer!</h1>
</body>
</html>

Опубликуйте созданный форк в своем репозитории и предоставьте ответ в виде ссылки на https://hub.docker.com/username_repo.

https://hub.docker.com/repository/docker/gkublock/devops-netology/general

Задача 2

Посмотрите на сценарий ниже и ответьте на вопрос: "Подходит ли в этом сценарии использование Docker контейнеров или лучше подойдет виртуальная машина, физическая машина? Может быть возможны разные варианты?"

Детально опишите и обоснуйте свой выбор.

--

Сценарий:

    Высоконагруженное монолитное java веб-приложение;
    Nodejs веб-приложение;
    Мобильное приложение c версиями для Android и iOS;
    Шина данных на базе Apache Kafka;
    Elasticsearch кластер для реализации логирования продуктивного веб-приложения - три ноды elasticsearch, два logstash и две ноды kibana;
    Мониторинг-стек на базе Prometheus и Grafana;
    MongoDB, как основное хранилище данных для java-приложения;
    Gitlab сервер для реализации CI/CD процессов и приватный (закрытый) Docker Registry.


1) Высоконагруженное монолитное java веб-приложение; Паравиртуализация или физический, т.к. приложение монолитное и нужна максимальная производительность
2) Nodejs веб-приложение; Docker идеально подходит, т.к. уже подходит под определение микросервиса
3) Мобильное приложение c версиями для Android и iOS; Зависит от архитектуры приложения, если на потребительском устройстве ставится UI с обращением к серверной части, и при этом функционал приложение разделен на микросервисы то можно и в docker, в иных случаях все таки виртуализация
4) Шина данных на базе Apache Kafka; Виртуализация. Большой поток данных, высокая нагрузка на диск.
5) Elasticsearch кластер для реализации логирования продуктивного веб-приложения - три ноды elasticsearch, два logstash и две ноды kibana; Elastic+logstash виртуализация/физика, т.к. опять же высоконагруженные сервисы и работают напрямую с поступающими+хранящимися данными, kibana в контейнере
6) Мониторинг-стек на базе Prometheus и Grafana; Тут можно в контейнер, т.к. если правильно помню метрики собираются при помощи агентов, и нагрузка как следствие будет меньше
7) MongoDB, как основное хранилище данных для java-приложения; Как и со всеми БД, для тестовых контуров можно docker, для нагрузки и прода уже лучше виртуализация/физический
8) Gitlab сервер для реализации CI/CD процессов и приватный (закрытый) Docker Registry. Сильно зависит от нагрузки и доступности. Если для небольшой команды, то подойдет и в контейнере
Задача 3

    Запустите первый контейнер из образа centos c любым тэгом в фоновом режиме, подключив папку /data из текущей рабочей директории на хостовой машине в /data контейнера;
    Запустите второй контейнер из образа debian в фоновом режиме, подключив папку /data из текущей рабочей директории на хостовой машине в /data контейнера;
    Подключитесь к первому контейнеру с помощью docker exec и создайте текстовый файл любого содержания в /data;
    Добавьте еще один файл в папку /data на хостовой машине;
    Подключитесь во второй контейнер и отобразите листинг и содержание файлов в /data контейнера.

---------------Centos-------------------
[root@522e66198fc1 data]# touch test-centos  
[root@522e66198fc1 data]# ls / | grep data
data
[root@522e66198fc1 data]# 

-----------------Debian------------
[gkublock@fedora devops-netology_ti_lisitsyn]$ sudo docker run -v /data:/data:z -d debian sleep infinity
fb1b17553d59d79e23019525de59187a2cfb2d7b4db83ed9e452cb2722008f99
[gkublock@fedora devops-netology_ti_lisitsyn]$ sudo docker exec -it fb1b17553d59d79e23019525de59187a2cfb2d7b4db83ed9e452cb2722008f99 bash
root@fb1b17553d59:/# touch /data/test_debian
root@fb1b17553d59:/# ls /data/
1  host_test  test-centos  test_debian

------------------Host--------------
[gkublock@fedora devops-netology_ti_lisitsyn]$ sudo touch /data/host_new_test
[gkublock@fedora devops-netology_ti_lisitsyn]$ sudo docker exec -it fb1b17553d59d79e23019525de59187a2cfb2d7b4db83ed9e452cb2722008f99 bash
root@fb1b17553d59:/# ls /data/
1  host_new_test  host_test  test-centos  test_debian




