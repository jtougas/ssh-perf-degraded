FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y \
        python3 \
        python3-dev \
        python3-pip
RUN apt-get update && apt install -y curl
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/srv/poetry python3 - --version 1.2.0
ENV PATH=/srv/poetry/bin:$PATH