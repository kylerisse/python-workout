# python-workout

Exercises for Python Workout by Reuven M Lerner. (https://www.goodreads.com/book/show/48505808-python-workout)

We used this book in our Q4 2020 study group. My personal goal was to learn the material as well as new techniques for unit testing. To that end, I aimed to complete all base exercise requirements with 100% test coverage and Circle CI integration.

## Requirements

* Docker

## Usage

* make build - builds docker image
* make lint - runs pylint (requires make build)
* make test - runs coverage/pytest (requires make build)
* make clean - removes python caches
* make mrproper - removes python caches and docker images
* make all - runs everything in order
* bin/copy_reports.sh - runs a silent make test and exports the coverage report to htmlcov (used by circle for web artifacts)  
