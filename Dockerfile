FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN python -m unittest discover -s /app/tests

CMD ["python", "/app/main.py"]
