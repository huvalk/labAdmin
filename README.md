### Шаги для подключения к внешней базе
1. Создать проект 
    `django-admin startproject adminPanel .`
   
2. Создать приложение
    `python manage.py startapp labTelegramBot`
   
3. Можно проанализировать базу
    `python manage.py inspectdb > models.py`
   
4. Создать модель в models.py

5. Создать роутер в dbrouters.py
   
6. Добавить в setting.py внешнюю базу и роутер
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite',
    },
    'telegramBot': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'students.db',
    }
}
DATABASE_ROUTERS = [
    'labTelegramBot.dbrouters.BotRouter',
]
```

7. Добавить в админку модели в admins.py
   
8. Миграции можно подделывать 
   `python manage.py migrate --fake labTelegramBot`