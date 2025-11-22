ARG UV_VERSION="0.7.21"
FROM ghcr.io/astral-sh/uv:${UV_VERSION} AS uv

FROM python:3.14 AS main

ENV TZ=Europe/Berlin
# RUN env | grep -i proxy

# RUN apt-get update && apt-get install -y --no-install-recommends \
#     vim \
#     && rm -rf /var/lib/apt/lists/*

RUN mkdir /app

RUN mkdir -p /app/data

COPY  . /app

# RUN chmod -R 777 /app

WORKDIR /app

ENV PYTHONPATH="/app:$PYTHONPATH"

RUN --mount=from=uv,source=/uv,target=/bin/uv \
    echo "Using uv from mounted image" && \
    uv --version || echo "uv command not found, using fallback" && \
    uv sync 

# RUN echo "Listing contents of .venv/bin:" && ls -l .venv/bin
ENV PATH="/app/.venv/bin:$PATH"

CMD uvicorn time_tracking.main:app --host 0.0.0.0 --port 8000
