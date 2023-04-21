Python version 3.10
Django version 4.0.5

Для работы проекта необходимо:

1. Установить библиотеку Django
# pip install django
2. Установить пакет allauth
# pip install django-allauth
3. Установить ckeditor
pip install django-ckeditor
4. Установить библиотеку celery
# pip install celery(5.2.7)
6. Установить библиотеку redis
# pip install redis
7. Установить сервер redis на локальной машине (OS Windows 10):
   - Устанавливаем пакетный менеджер Chocolatey для работе в среде
      Windows в следующем порядке:
      - Запускаем PowerShell
      - Убедиться, что Get-ExecutionPolicy не является Restricted
      - Командой Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]:
        :SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).
        DownloadString('https://chocolatey.org/install.ps1')) установим Chocolatey.
   - На официальном сайте Chocolatey находим подходящую версию Redis - в данном случае:
     https://chocolatey.org/packages/redis-64/3.0.503
   - Затем вводим скопированную команду из буфера обмена (Ctrl-V) в консоль PowerShell:
     choco install redis-64 --version 3.0.503
   - Сервер Redis командой в PowerShell: redis-server
     В консоли PowerShell должно появиться сообщение о том, что сервер Redis работает и принимает соединения.
   - После этого откройте ещё одно окно Powershell, не закрывая окно с запущенным сервером. В новом выполните команду:
     redis-cli
     Теперь можно использовать redis в командной строке для работы с сервером Redis
8. Запустить первый терминал python manage.py runserver
9. Запустить Celery во втором терминале celery -A MMORPG_board worker -l INFO
10.Запустить команду celery -A MMORPG_boar beat -l INFO

