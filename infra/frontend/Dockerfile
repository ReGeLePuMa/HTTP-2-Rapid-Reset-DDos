FROM nginx:alpine

COPY ./dist/ /usr/share/nginx/html/
COPY ./certs /etc/ssl/certs/
COPY ./nginx.conf /etc/nginx/conf.d/default.conf