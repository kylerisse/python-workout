#!/usr/bin/bash

CONTAINER=$(docker run -d python-workout pytest --json-report -vv)
sleep 5
docker cp ${CONTAINER}:/app/.report.json ./
