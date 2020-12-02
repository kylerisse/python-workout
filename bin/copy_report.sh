#!/usr/bin/bash

echo "generating HTML report..."
CONTAINER=$(docker run -d python-workout sh -c 'coverage run -m pytest -vv && coverage html')
sleep 12
docker cp ${CONTAINER}:/app/htmlcov ./
