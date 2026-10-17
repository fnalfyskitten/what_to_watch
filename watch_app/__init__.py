# watch_app/__init__.py

import os
from dotenv import load_dotenv  # <-- 1. Импортируем функцию загрузки
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# <-- 2. САМОЕ ВАЖНОЕ: Загружаем переменные из .env СРАЗУ при старте
# Эта строка должна быть одной из самых первых в файле!
load_dotenv() 

app = Flask(__name__)

# <-- 3. Теперь берем ключ из переменных окружения
# Если ключа нет в .env, можно задать запасной вариант для безопасности
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'fallback-secret-key-if-missing')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

from . import views, models
