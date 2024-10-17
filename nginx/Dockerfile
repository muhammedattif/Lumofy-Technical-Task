FROM nginx:1.25.3-alpine as base
RUN rm /etc/nginx/conf.d/default.conf

###### Nginx Local
FROM base as nginx-local
COPY nginx-local.conf /etc/nginx/conf.d


###### Nginx Staging and Prod
FROM base as nginx
COPY nginx-selfsigned.crt /etc/ssl/certs/nginx-selfsigned.crt
COPY nginx-selfsigned.key /etc/ssl/private/nginx-selfsigned.key
COPY dhparam.pem /etc/ssl/certs/dhparam.pem
COPY ssl-params.conf /etc/nginx/snippets/ssl-params.conf
COPY uwsgi_params /etc/nginx/snippets/uwsgi_params
COPY nginx.conf /etc/nginx/conf.d
