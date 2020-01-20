NAME = `basename ${CURDIR}`
build:
	@docker build . -t ${NAME}

pelican:
	@docker run -it --rm \
	-v ${CURDIR}:/app \
	-p 8000:8000 \
	${NAME} pelican content -s pelicanconf.py -v -r -l -b 0.0.0.0

cli:
	@docker run -it --rm \
	-v ${CURDIR}:/app \
	${NAME}
