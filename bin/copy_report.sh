#!/usr/bin/bash

CONTAINER=$(docker run -d python-workout sh -c 'coverage run -m pytest -vv && coverage html')
sleep 10 
docker cp ${CONTAINER}:/app/htmlcov ./
