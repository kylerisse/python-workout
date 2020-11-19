build: clean
	docker build -t python-workout .

test: clean
	# make: test (requires make build)
	docker run -ti python-workout sh -c 'coverage run -m pytest -vv && coverage report'

lint: clean
	# make: lint (requires make build)
	docker run -ti python-workout sh -c 'pylint *.py'

clean:
	# make: clean
	rm -rf htmlcov/
	rm -rf __pycache__
	rm -rf src/__pycache__
	rm -rf .pytest_cache
	rm -rf src/.pytest_cache

mrproper: clean
	# make: mrproper
	docker rmi -f python-workout

all: mrproper build lint test
	# make: all
