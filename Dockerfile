FROM python:3.9.10-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./

ENV FLASK_APP "app.main:app"
VOLUME [ "/data" ]
CMD flask db upgrade && \
    gunicorn -b 0.0.0.0:8000 -w 1 app.main:app
EXPOSE 8000
