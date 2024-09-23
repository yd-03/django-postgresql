import os
from pathlib import Path

# プロジェクトのベースディレクトリを設定
BASE_DIR = Path(__file__).resolve().parent.parent

# 環境変数からシークレットキーを取得
SECRET_KEY = os.environ.get("SECRET_KEY")

# 環境変数からデバッグモードを設定
DEBUG = os.environ.get("DEBUG") == "True"

# 環境変数から許可するホストを設定
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "").split(",")

# インストールされているアプリケーション
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# ミドルウェアの設定
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ルートURL設定
ROOT_URLCONF = "djangopj.urls"

# テンプレート設定
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGIアプリケーションの設定
WSGI_APPLICATION = "djangopj.wsgi.application"

# データベースの設定
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_NAME"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": "db",
        "PORT": 5432,
        "OPTIONS": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# パスワードバリデーションの設定
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# 言語コードの設定
LANGUAGE_CODE = "ja"

# タイムゾーンの設定
TIME_ZONE = "Asia/Tokyo"

# 国際化の設定
USE_I18N = True

# ローカライズの設定
USE_L10N = True

# タイムゾーンの使用設定
USE_TZ = True

# 静的ファイルのルートディレクトリ
STATIC_ROOT = "/static/"

# 静的ファイルのURL
STATIC_URL = "/static/"

# デフォルトの自動フィールドタイプ
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
