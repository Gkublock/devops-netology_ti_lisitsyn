# devops-netology_ti_lisitsyn
Netology tasks, owner is TI_Lisitsyn
Files to ignore:
./idea
./terraform/test


Задача 1

    Опишите своими словами основные преимущества применения на практике IaaC паттернов.
    Какой из принципов IaaC является основополагающим?
Преимущества следующие:
1) Ускорение процесса разработки и получения конечного результата
При использовании подхода IaaC мы получаем преимущество в виде того, что вся инфраструктура
разворачивается набором команд. И если требуются какие-либо специфичные настройки, увеличить масштаб инфраструктуры,
их не надо будет вопроизводить
поштучно на каждом из серверов инфраструктуры
2) Стабильность
Т.к. вся инфра у нас выходит "близнецами", куда проще предугадать поведение на промышленных стендах

Основным принципом является обеспечение идемпотентности.

Задача 2

    Чем Ansible выгодно отличается от других систем управление конфигурациями?
    Какой, на ваш взгляд, метод работы систем конфигурации более надёжный push или pull?
Простота в обращении и настройке. Ансибл использует python, который по умолчанию установлен
на всех linux дистрибутивах и подключение по ssh, которое тоже является частью дистрибутива
Для начала пользования требуется исключительно установка ansible на сервер, у которого есть ssh доступ до целевых ресурсов


Задача 3

Установить на личный компьютер:

    VirtualBox
    Vagrant
    Ansible



Приложить вывод команд установленных версий каждой из программ, оформленный в markdown.
[gkublock@fedora devops-netology_ti_lisitsyn]$ ansible --version
ansible [core 2.13.5]
  config file = None
  configured module search path = ['/home/gkublock/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /home/gkublock/.local/lib/python3.10/site-packages/ansible
  ansible collection location = /home/gkublock/.ansible/collections:/usr/share/ansible/collections
  executable location = /home/gkublock/.local/bin/ansible
  python version = 3.10.7 (main, Sep  7 2022, 00:00:00) [GCC 12.2.1 20220819 (Red Hat 12.2.1-1)]
  jinja version = 3.1.2
  libyaml = True
[gkublock@fedora devops-netology_ti_lisitsyn]$ vagrant --version
Vagrant 2.2.19
[gkublock@fedora devops-netology_ti_lisitsyn]$ vboxmanage --version
7.0.2r154219
[gkublock@fedora devops-netology_ti_lisitsyn]$ 
