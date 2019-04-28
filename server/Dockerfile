FROM python:3.7-alpine

ENV PYTHONUNBUFFERED=true
ENV PYTHONIOENCODING=utf-8

WORKDIR /opt/kuluserver
COPY . .

RUN apk add py3-pip gcc postgresql-dev musl-dev libffi-dev libressl-dev && \
    pip3 install -r requirements.txt

CMD python3 -m kuluserver
