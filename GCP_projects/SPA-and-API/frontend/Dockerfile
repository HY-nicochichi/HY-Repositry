FROM nginx:1.27-alpine

EXPOSE 8080

COPY vueapp/dist /usr/share/nginx/html
COPY default.conf /etc/nginx/conf.d

CMD ["nginx", "-g", "daemon off;"]
