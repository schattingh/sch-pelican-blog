FROM python:3-slim

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
  apt-get install \
  ca-certificates \
  cmake gcc \
  curl \
  libjpeg62-turbo-dev \
  wget \
  zlib1g-dev \
  --no-install-recommends -y

#  Install from source to use jpeg-turbo
RUN pip install Pillow --no-binary :all:

RUN pip install pelican[Markdown] beautifulsoup4

WORKDIR /app

CMD [ "pelican", "content", "-s", "pelicanconf.py", "-v", "-r", "-l", "-b", "0.0.0.0" ]
