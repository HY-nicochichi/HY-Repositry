# Nuxt-Rails/frontend

## Dockerfile 初回起動時のコード
FROM node:22.11.0-bookworm-slim
CMD npx nuxi@3.22.5 init nuxtapp --package-manager npm --git-init false

## 初回起動後ローカルPCで実行
docker cp frontend-container-ID:/nuxtapp ./frontend
