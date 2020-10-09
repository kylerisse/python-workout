FROM python:3.8.6-alpine
RUN apk --update add pytest py3-pip
COPY ./ /app
WORKDIR /app
RUN pip install -r requirements.txt 
