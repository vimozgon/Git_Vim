
Как системному администратору данной организации вам поставлена задача собрать на докер образ Django 
(Linux, nginx, Django, Postgres, Gunicorn) сервера. Все нужные сервисы должны быть проброшены на хост по стандартным 
портам, реализация HTTPS не требуется, версии Django, nginx и Postgres не имеют значения, как и версия ядра Linux. 
В проекте просто должна работать админка с заранее прописанным логином и паролем.


## Установка docker
Для lunix систем:   
```curl -fsSL https://get.docker.com/ | sh``` //Установка Docker  
Для Windows или Macos:  
```https://www.docker.com/``` //Установка Docker Desktop  

## Запуск приложения:  
После установки docker, загружаем проект командой:  
`git clone https://github.com/vimozgon/Git_Vim/SF_G4.10.git`  
В командной строке из директории с скопированным проектом:  
`sudo docker-compose up -d`  //Для lunix
`docker-compose up -d` //Docker Desktop (Windows)
После  установки и запуска контейнеров, заходим в браузере по адресу:  

http://localhost:1337  

Войти на страницу администрирования можно по адресу:  
http://localhost:1337/admin 

Учетные данные: 
логин: admin  
пароль: admin  

