FROM python:3.8.6-alpine
COPY ./ /app
WORKDIR /app
RUN pip install -r requirements.txt 
