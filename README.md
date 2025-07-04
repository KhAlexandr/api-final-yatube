# API для социальной сети Yatube

## Описание

API для соцсети блогеров Yatube.Проект реализован на REST API DJANGO.
  
#### Доступный функционал

- Для аутентификации используются JWT-токены.
- У неаутентифицированных пользователей доступ к API только на уровне чтения.
- Для эндпойнта /follow/ установлено дополнительное ограничение.Доступ к нему только у аутентифицированных пользователей.
- Аутентифицированным пользователям разрешено изменение и удаление своего контента, в остальных   случаях доступ предоставляется только для чтения.
- Подписки на пользователей.
- Просмотр, создание, изменение и удаление записей.
- Просмотр и создание групп.
- Возможность добавления, редактирования, удаления своих комментариев и просмотр чужих.
- Фильтрация по полям.

#### Документация к API доступна по адресу [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/) после запуска сервера с проектом

#### Технологии

- Python 3.12
- Django 5.1.1
- Django Rest Framework 3.15.2
- Djoser 2.3.1
- Simple JWT

#### Запуск проекта в dev-режиме

- Склонируйте репозиторий:  
``` git clone <название репозитория> ```    
- Установите и активируйте виртуальное окружение:  
``` python -m venv venv ```  
``` source venv/Scripts/activate ``` 
- Установите зависимости из файла requirements.txt:   
``` pip install -r requirements.txt ```
- Перейдите в папку api_yatube/yatube_api.
- Примените миграции:   
``` python manage.py migrate ```
- Выполните команду:   
``` python manage.py runserver ```

#### Примеры некоторых запросов API

Получить список всех постов:  
```
GET /api/v1/posts/ 

{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```  
Добавление нового поста:  
```
POST /api/v1/posts/

{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```   
Получить список всех групп:  
```
GET /api/v1/groups/

[
  {
    "id": 0,
    "title": "string",
    "slug": "^-$",
    "description": "string"
  }
]
```  
Добавление нового комментария:  
```
POST /api/v1/posts/{post_id}/comments/

{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```  
Удаление комментария по id:  
```
DELETE /api/v1/posts/{post_id}/comments/{id}/

{
  "detail": "Учетные данные не были предоставлены."
}
```  
Получение списока подписок:  
```
GET /api/v1/follow/

[
  {
    "user": "string",
    "following": "string"
  }
]
```  
Подписка пользователя на пользователя переданного в запросе:  
```
POST /api/v1/follow/

{
  "user": "string",
  "following": "string"
}
```  

#### Автор

Хачатурян Александр - https://github.com/KhAlexandr

