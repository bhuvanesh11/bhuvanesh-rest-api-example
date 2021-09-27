FROM python:3.8.6-alpine3.12

COPY . .

RUN apk add --no-cache curl g++ gcc libffi-dev libressl-dev musl-dev git cargo && \
    pip3 install --upgrade pip && \
    pip3 install -r requirements.txt  --no-cache-dir

ENV PYTHONPATH=.

EXPOSE 5000

ENTRYPOINT ["python", "app/routes.py"]
