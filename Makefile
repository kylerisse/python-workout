.PHONY: build
build: clean
	docker build -t python-workout .

.PHONY: test
test: clean
	# make: test (requires make build)
	docker run -ti python-workout pytest -vv

.PHONY: lint
lint: clean
	# make: lint (requires make build)
	docker run -ti python-workout pylint *.py

.PHONY: clean
clean:
	# make: clean
	rm -rf __pycache__
	rm -rf .pytest_cache

.PHONY: mrproper
mrproper: clean
	# make: mrproper
	docker rmi -f python-workout

.PHONY: all
all: mrproper build lint test
	# make: all
