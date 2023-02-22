![Документация](head.jpg)
# Учебный проект по «API для Yatube»

:small_orange_diamond: **Пояснение.**
> Yatube социальная сеть реализованная на фреймворке Django.
API для неё реализованно на Django Rest Framework (DRF).

Целью проекта является создание API для Yatube. При помощи такой мощной разработки,
мы без проблем, сможем подружить бэкенд с фронтендом!!! :fire:

:yellow_circle: Когда вы запустите проект, по адресу  http://127.0.0.1:8000/redoc/ будет доступна :book: документация для API

:yellow_circle: Для аутентификации используются JWT-токены, реализованно при помощи библиотеки Djoser. 


## Как запустить проект:

### Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/SlemCool/api_final_yatube.git
```

```
cd api_final_yatube
```

### Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
. venv/Scripts/activate
```

### Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

### Выполнить миграции:

```
python manage.py migrate
```

### Запустить проект:

```
python manage.py runserver
```
