#!/bin/sh

# データベースのマイグレーションと静的ファイルの収集
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput

# DEBUG環境変数に基づいてサーバーを起動
if [ "$DEBUG" = "1" ]; then
    python manage.py runserver 0.0.0.0:8000
else
    gunicorn djangopj.wsgi:application --bind 0.0.0.0:8000
fi