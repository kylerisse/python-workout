FROM python:3.8.6-alpine
COPY src/ /app/
WORKDIR /app
RUN pip install -r requirements.txt 
