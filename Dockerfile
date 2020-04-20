FROM python:3.8.2-slim-buster
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP app.py
ENV PORT 5000
ENV TZ Asia/Tokyo

COPY ./requirements.txt app.py /usr/src/app/
RUN pip install --upgrade pip \
  && pip install -r requirements.txt
EXPOSE $PORT
CMD flask run -h 0.0.0.0 -p $PORT
