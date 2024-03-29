Бэкап базы [django_ads_db.sql1.sql](django_ads_db.sql1.sql)
<details>
<summary>Пункты 1-5 ...</summary>

### 1. Модель пользователя переписана на наследование от AbstraсtUser
Создание пользователя

**Request:**  POST /user/
```
{
    "password": "zxcvb68",
    "username": "oleg68"
}
```

### 2. Авторизация по JWT

**Request:**  POST /user/token/
```
{
    "password": "rthg125",
    "username": "petr555"
}
```
**Request:**  POST /user/token/refresh/
```
{
    "refresh": "(JWT_token refresh из предыдущего запроса)"
}
```

### 3. Просмотр детальной информации об объявлении только авторизованным пользователем

**Request:**  GET /ad/11

`Без указания заголовка авторизации получим ответ "Учетные данные не были предоставлены."`

**Request:**  GET /ad/11

**Headers:** Authorization: Bearer (JWT_token из запроса токена petr555)

`Получим детальную информацию об объявлении`

### 4. Подборки объявлений

- Показываем список подборок без авторизации

**Request:**  GET /selection/

`Получаем список подборок без подробной информации`

- Показываем подробную информацию о конкретной подборке только авторизованному пользователю

**Request:**  GET /selection/4/

**Headers:** Authorization: Bearer (JWT_token из запроса токена petr555)

`Получаем детальную информацию о подборке с подробной информацией по каждому объявлению из подборки.
Без указания заголовка авторизации получим ответ "Учетные данные не были предоставлены."`

- Создание подборки авторизованным пользователем

**Request:** POST /selection/

**Headers:** Authorization: Bearer (JWT_token из запроса токена petr555)
```
{
    "name": "Объявления о котиках",
    "items": [1, 7, 20]
}
```
- Редактирование только своей подборки

Пытаемся редактировать чужую подборку

**Request:**  PUT /selection/4/

**Headers:** Authorization: Bearer (JWT_token из запроса токена petr555)
```
{
    "owner":"pavel123",
    "name": "Подборка Павла",
    "items": [2, 4, 6]
}
```
Теперь свою

**Request:**  PUT /selection/5/

**Headers:** Authorization: Bearer (JWT_token из запроса токена petr555)
```
{
    "owner":"petr555",
    "name": "Подборка Петра разное",
    "items": [8, 6, 12]
}
```

- Удаление только своей подборки

Пытаемся удалить чужую подборку

**Request:**  DELETE /selection/4/

**Headers:** Authorization: Bearer (JWT_token из запроса токена petr555)

Теперь свою

**Request:**  DELETE /selection/5/

**Headers:** Authorization: Bearer (JWT_token из запроса токена petr555)

### 5. Редактировать и удалять объявление могут автор либо модератор или админ
- Получаем токен для не автора объявления и не модератора и не админа

**Request:**  POST /user/token/
```
{
    "password": "rthg125",
    "username": "petr555"
}
```
**Request:**  PUT /ad/11/

**Headers:** Authorization: Bearer (JWT_token из запроса токена)
```
{   
    "author": "petr_bo",
    "category": "Мебель и интерьер",
    "name": "Стол из слэба и эпоксидной смолы",
    "price": 20000,
    "description": "Отличный стол",
    "is_published": true,
    "image": "http://127.0.0.1:8000/media/images/post11.jpg"
}
```
- Теперь изменяем объявление, у которого этот юзер автор

**Request:**  PUT /ad/29/

**Headers:** Authorization: Bearer (JWT_token из запроса токена)
```
{
    "author": "petr555",
    "category": "Котики",
    "name": "пушистик",
    "price": 500,
    "description": "Самый веселый котик",
    "is_published": true,
    "image": null
}
```
- Получаем токен для модератора

**Request:**  POST /user/token/
```
{
    "password": "12345",
    "username": "pavel123"
}
```
**Request:**  DELETE /ad/29/

**Headers:** Authorization: Bearer (JWT_token из запроса токена)
</details>

### 6. Валидация
- Добавьте поле slug, длина которого не более 10 символов, а значения уникальны

**Request:**  POST /cat/create/
```
{
    "name": "Котики1",
    "slug": "catss"
}
```
такой слаг уже есть в базе
```
{
    "name": "Бытовая техника",
    "slug": "home_appliances"
}
```
```
{
    "name": "Бытовая техника",
    "slug": "appliance"
}
```
- Поле name объявления не может быть пустым и должно содержать не менее 10 символов.

**Request:**  POST /ad/
```
{
    "category": "Котики",
    "name": "Котята",
    "price": 500,
    "is_published": false
}
```
- Поле description объявления может быть пустым

**Request:**  POST /ad/
```
{
    "category": "Котики",
    "name": "Котята в хорошие руки",
    "price": 500,
    "is_published": false
}
```
- Значение поля price объявления не может быть меньше 0.

**Request:**  POST /ad/
```
{
    "category": "Котики",
    "name": "Котята в хорошие руки",
    "price": -500,
    "is_published": false
}
```
- Значение поля is_published при создании объявления не может быть True

**Request:**  POST /ad/
```
{
    "category": "Котики",
    "name": "Сибирский кот",
    "price": 500,
    "is_published": true
}
```
- Добавьте пользователям поле birth_date и запретите регистрироваться пользователям младше 9 лет.
**Request:**  POST /user/
```
{
    "password": "456238",
    "username": "serg888",
    "email": "serg888@yandex.ru",
    "birthday": "2018-10-15"
}
```

- Добавьте поле email, сделайте его уникальным и запретите регистрацию с почтового адреса в домене rambler.ru

**Request:**  POST /user/
```
{
    "password": "12345",
    "username": "oleg168",
    "email": "petr5@yandex.ru"
}
```
Такой email есть в базе

**Request:**  POST /user/
```
{
    "password": "12345",
    "username": "oleg168",
    "email": "petr5@rambler.ru"
}
```

### 7. Тесты
Покрыть тестами:
- создание объявления — POST `/ads`;
- создание подборки — POST `/selection`;
- выдачу списка объявлений (без фильтров) — GET `/ads`;
- выдачу одного объявления — GET `/ads/<ad_id>`.

![python img](Test_paased.png)
