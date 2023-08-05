FROM python:3.10-slim-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV REDIS_URL redis:6379
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . .
# COPY entrypoint.sh /entrypoint.sh
# RUN chmod +x ./docker-entrypoint.sh
# ENTRYPOINT "./docker-entrypoint.sh"