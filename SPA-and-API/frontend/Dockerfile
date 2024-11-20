FROM nginx:1.27.2-alpine3.20

COPY vueapp/dist /usr/share/nginx/html
COPY default.conf /etc/nginx/conf.d

CMD ["nginx", "-g", "daemon off;"]
