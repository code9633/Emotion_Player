FROM python:3.11.5

ENV PYTHONBUFFERED = 1

WORKDIR /EmoPlayer

COPY ./ ./

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]

