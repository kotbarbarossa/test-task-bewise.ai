# Тестовое задание для bewise.ai

> Задача создать сервис получающий вопросы и ответы для викторины с публичного API `https://jservice.io/api/`.
Функционал сервиса заключается в добавлении заданного в запросе числа вопросов в базу данных проекта.

[![N|Solid](https://jservice.io/images/trebek.png)](https://jservice.io/)

#### Описание

Проект реализован на стеке:
- Python
- Django REST Framework
- Docker-Compose
- PostgreSQL
- Nginx
- Gunicorn

### Запуск:

Для запуска проекта необходимо установить **[Docker-Compose]**.
Далее склонировать репозиторий:
```bash
git clone https://github.com/kotbarbarossa/test-task-bewise.ai.git
```
и перейти папку `infra`.

Для успешного запуска предварительно необходимо создать файл с переменными окружения `.env`:
```markdown
/infra/.env
```
Шаблон для заполнения файла:

```dotenv
SECRET_KEY = 'django-insecure-7$taod2usv$x_rs5*@#42mo&gc%b0v1-yq8v^5s7+8*d#qx1wc'
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

Для запуска образа необходимо ***в папке infra*** ввести команду:
```sh
docker-compose up -d
```
#### Подготовка

После разворачивания контейнеров нужно выполнить **миграции** и создать пользователя.

Запуск командной строки контейнера с backend:
```sh
docker exec -it backend bash
```
Миграции:
```sh
python manage.py migrate
```
Создание пользователя:
```sh
python manage.py createsuperuser
```


#### Использование

Для взаимодействия с сервисом необходимо отправить POST запрос на эндпоинт `http://localhost/api/v1/questions-number/`
или
`http://<IP-адрес-сервера>/api/v1/questions-number/`
Тело запроса должно иметь вид:
```json
{
    "questions_num": integer
} 
```
где в качестве параметра integer должно быть передано целое положительное число.

Пример ответа от сервиса имеет вид:

```json
{
    "result": "Вопросы успешно сохранены в базе",
    "previous_question": {
        "id": "182546",
        "question": "The third-stage engine of this type of rocket used for Apollo flights to the moon kicked things to 25,000 MPH",
        "answer": "Saturn",
        "created_at": "2022-12-30T21:21:36.063000Z"
    }
}
```

где в параметре `"previous_question"` находится предыдущий сохранённый объект викторины. В случае его отсутствия - ***пустой объект***.

Для полноценного взаимодействия с базой необходимо перейти в админ зону находящуюся по адресу `http://localhost/admin/` или `http://<IP-адрес-сервера>/admin/`
и воспользоваться логином и паролем введенными ранее.

#### Автор 

**Эльдар Барбаросса** 
[INSTAGRAM]
telegram @kotopro

[//]: # (links)

[youtube]: https://www.youtube.com/channel/UC0NWbtRrU1YvsCP_0Slq-9A/
[INSTAGRAM]: https://instagram.com/kot.barbarossa?igshid=YmMyMTA2M2Y=
[Docker-Compose]: <https://docs.docker.com/compose/>
