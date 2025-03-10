API для социальной сети Yatube
Описание
API для соцсети блогеров Yatube.Проект реализован на REST API DJANGO.

Доступный функционал
Для аутентификации используются JWT-токены.
У неаутентифицированных пользователей доступ к API только на уровне чтения.
Для эндпойнта /follow/ установлено дополнительное ограничение.Доступ к нему только у аутентифицированных пользователей.
Аутентифицированным пользователям разрешено изменение и удаление своего контента, в остальных случаях доступ предоставляется только для чтения.
Подписки на пользователей.
Просмотр, создание, изменение и удаление записей.
Просмотр и создание групп.
Возможность добавления, редактирования, удаления своих комментариев и просмотр чужих.
Фильтрация по полям.
Документация к API доступна по адресу http://127.0.0.1:8000/redoc/ после запуска сервера с проектом

Технологии:

asgiref==3.8.1
attrs==24.2.0
certifi==2024.12.14
cffi==1.17.1
charset-normalizer==3.4.1
coreapi==2.3.3
coreschema==0.0.4
cryptography==44.0.0
defusedxml==0.7.1
Django==5.1.1
django-templated-mail==1.1.1
djangorestframework==3.15.2
djangorestframework_simplejwt==5.4.0
djoser==2.3.1
flake8==7.1.1
idna==3.10
iniconfig==2.0.0
itypes==1.2.0
Jinja2==3.1.5
MarkupSafe==3.0.2
mccabe==0.7.0
oauthlib==3.2.2
packaging==24.2
pillow==11.0.0
pluggy==1.5.0
py==1.11.0
pycodestyle==2.12.1
pycparser==2.22
pyflakes==3.2.0
PyJWT==2.10.1
pyparsing==3.2.1
pytest==8.3.3
pytest-django==4.9.0
pytest-pythonpath==0.7.3
python3-openid==3.2.0
pytz==2024.2
requests==2.32.3
requests-oauthlib==2.0.0
six==1.17.0
social-auth-app-django==5.4.2
social-auth-core==4.5.4
sqlparse==0.5.2
toml==0.10.2
uritemplate==4.1.1
urllib3==2.3.0

Запуск проекта в dev-режиме

Склонируйте репозиторий:
git clone <название репозитория>
Установите и активируйте виртуальное окружение:
python -m venv venv
source venv/Scripts/activate
Установите зависимости из файла requirements.txt:
pip install -r requirements.txt
Перейдите в папку api_yatube/yatube_api.
Примените миграции:
python manage.py migrate
Выполните команду:
python manage.py runserver
Примеры некоторых запросов API
Получить список всех постов:
GET /api/v1/posts/
Добавление нового поста:
POST /api/v1/posts/
Получить список всех групп:
GET /api/v1/groups/
Добавление нового комментария:
POST /api/v1/posts/{post_id}/comments/
Удаление комментария по id:
DELETE /api/v1/posts/{post_id}/comments/{id}/
Получение списока подписок:
GET /api/v1/follow/
Подписка пользователя на пользователя переданного в запросе:
POST /api/v1/follow/