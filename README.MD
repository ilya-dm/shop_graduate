Инструкция по запуску проекта:
1. с помощью команды `pip install -r requirements.txt` установить необходимые зависимости
2. провести миграции `python.manage.py makemigrations`
`python manage.py migrate`
3. заполнить БД тестовыми данными `python manage.py loaddata fixtures.json`
4. Запустить проект командой `python manage.py runserver`

Для администрирования будет доступен пользователь admin с паролем admin.
