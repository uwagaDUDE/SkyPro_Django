# SkyPro_Django

Учебный проект, в котором я учусь осваивать Django (Добавлять свои команды, заполнять БД)

## Установка

Для начала работы нужно установить PostgreSQL.

Установите зависимости, используя команду:

```bash
pip install -r requirements.txt
```

## Запуск

Запустите сервер, используя команду:

```bash
py manage.py runserver
```

## Список зависимостей

<details>
<summary>Зависимости</summary>

- asgiref==3.6.0
- asttokens==2.2.1
- backcall==0.2.0
- colorama==0.4.6
- decorator==5.1.1
- Django==4.2.1
- executing==1.2.0
- ipython==8.13.2
- jedi==0.18.2
- matplotlib-inline==0.1.6
- parso==0.8.3
- pickleshare==0.7.5
- Pillow==9.5.0
- prompt-toolkit==3.0.38
- psycopg2==2.9.6
- pure-eval==0.2.2
- Pygments==2.15.1
- six==1.16.0
- sqlparse==0.4.4
- stack-data==0.6.2
- traitlets==5.9.0
- typing_extensions==4.5.0
- tzdata==2023.3
- wcwidth==0.2.6

</details>

## Использование

На данном этапе есть кастомная команда autoFill (вызываемая: `py manage.py autoFill`). Она добавляет товар в базу данных.
