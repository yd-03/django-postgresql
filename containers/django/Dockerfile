# ベースイメージとしてPython 3を使用
FROM python:3

# 環境変数設定
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 作業ディレクトリを設定
WORKDIR /code

# 必要なファイルをコピーし、依存関係をインストール
COPY requirements.txt /code/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# ソースコードとエントリーポイントスクリプトをコピーし、実行権限を付与
COPY . /code/
COPY ./containers/django/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh