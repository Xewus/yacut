# YaCut
Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

## Ключевые возможности сервиса
генерация коротких ссылок и связь их с исходными длинными ссылками,
переадресация на исходный адрес при обращении к коротким ссылкам.
Доступны web и api интерфейсы.

## Технологии
Python 3.10
Flask 2.0
Jinja2 3.0
SQLAlchemy 1.4
### Установка
Клонировать репозиторий и перейти в него в командной строке:

```
git clone 
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/MacOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
Создать файл настроек окруженияЖ
```
touch .env
```
Заполнить его:
```
FLASK_APP=yacut
FLASK_ENV=production
SQLALCHEMY_DATABASE_URI=<sqlite:///db.sqlite3>
SECRET_KEY=<Your secret key>
```
Запустить:
```
flask run
```
