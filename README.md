# Rerikom_test_task

Для запуска проекта нужно проделать следующие действия:
```
git clone https://github.com/yungalexxxey/Rerikom_test_task.git 
```
Затем:
```
sudo docker-compose up -d
```
Для подключения к базе данных (для проверки того, что всё работает):
```
psql "host=localhost \                                                                                                        ✔ 
port=5450 \
dbname=rerikom_db \
user=rerikom_user"
```
Пароль: pswrd 

# Про проектик
Всё запускается ( по крайней мере должно) в нужном порядке с помощью docker-compose. 
Затем, при добавлении нового сообщения в бд, сервис это сообщение "складывает" и в кафку. 
Listener в свою очередь при получении сообщения делает проверку на наличие зарпрёщенного слова в сообщении. Результат же отправляется POST запросом с зашифрованным JWT-токеном на сервис. Сервис же в свою очередь проверяет токен, проверяет корректность данных и меняет STATUS сообщения в базе данных.
Стек проекта:
- fastapi
- uvicorn
- pydantic
- requests
- sqlalchemy
- psycopg2
- pyjwt
- kafka-python
- Docker
- Docker-compose

