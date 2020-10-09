.PHONY: dockertest
dockertest:
	docker build -t test .
	docker run -ti test