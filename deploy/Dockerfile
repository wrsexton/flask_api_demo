FROM python:3.10-buster

EXPOSE 8005

USER root

RUN apt-get update && apt-get install libcurl4-openssl-dev postgresql libpq-dev --yes

WORKDIR /var/www

# Add current directory to PYTHONPATH
ENV PYTHONPATH /var/www
ENV PATH="/var/www/.local/bin:${PATH}"

COPY . .

USER www-data:www-data