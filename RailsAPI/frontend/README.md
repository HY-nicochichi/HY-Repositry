# RailsAPI/frontend

## Dockerfile 初回起動時のコード
FROM node:22.2-bookworm-slim
RUN npm install -g @vue/cli@5.0.8

## 初回起動後コンテナ内で実行
vue create vueapp (routerオプションも選択)

## 初回起動後ローカルPCで実行
docker cp frontend-container-ID:/vueapp ./frontend
