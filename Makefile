build:
	docker-compose build

pelican:
	docker-compose up

down:
	docker-compose down

shell:
	docker-compose run --rm --service-ports pelican bash

clean:
	rm -fr output/*
