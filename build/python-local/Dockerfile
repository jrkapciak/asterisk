FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y gcc \
    python3-dev \
    musl-dev \
    libmagic1 \
    libffi-dev \
    netcat-traditional \
    build-essential \
    libpq-dev

WORKDIR /app

COPY /poetry.lock pyproject.toml /app/

RUN pip3 install poetry \
    && poetry config virtualenvs.create false \
    &&  poetry install --with dev

RUN rm -rf /var/cache/apt/archives /var/lib/apt/lists/*

COPY ./build/python-local/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]