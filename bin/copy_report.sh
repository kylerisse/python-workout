#!/usr/bin/bash

CONTAINER=$(docker run -d python-workout pytest --junitxml=report.xml -vv)
sleep 5
docker cp ${CONTAINER}:/app/report.xml ./
