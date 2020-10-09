FROM python:3.8.6-alpine
RUN apk --update add pytest
COPY ./ /app
WORKDIR /app
CMD pytest -vv