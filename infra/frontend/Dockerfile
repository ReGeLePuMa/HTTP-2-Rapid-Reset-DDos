FROM nginx

RUN apt-get update && apt-get install -y \
    net-tools \
    iputils-ping \
    iproute2 \
    curl

COPY ./dist/ /usr/share/nginx/html/
COPY ./certs/ /etc/ssl/certs/
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
