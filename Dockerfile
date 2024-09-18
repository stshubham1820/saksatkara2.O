FROM python:3.12.0

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /saksatkara
COPY . /saksatkara/

RUN pip install -r requirements.txt

RUN pip install youtokentome

RUN pip install boto3

RUN apt-get update && apt-get install -y libsndfile1

RUN  apt-get update && apt-get install -y ffmpeg

COPY ./celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./celery/beat/start /start-celerybeat
RUN sed -i 's/\r$//g' /start-celerybeat
RUN chmod +x /start-celerybeat

COPY ./celery/flower/start /start-flower
RUN sed -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower