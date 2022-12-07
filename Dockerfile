FROM python:3.7.15-alpine

WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /app


COPY ../.. .

RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/

RUN pip install -r ./requirements.txt

# 设置时区为上海
RUN apk add -U tzdata && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && apk del tzdata



CMD ["python", "main.py"]