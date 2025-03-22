# RailsTrad/main

## Dockerfile 初回起動時のコード
FROM ruby:3.3.4-slim-bookworm
RUN apt-get update -qq && \ 
apt-get install -y build-essential libpq-dev git
COPY . /
WORKDIR /railsapp
RUN bundle install
RUN rails new . --force --skip-jbuilder --database=postgresql
RUN rails g model user mail:string name:string password_enc:string
RUN rm -r .git && rm README.md Dockerfile .dockerignore

## railsapp/Gemfile 初回起動時のコード(Gemfile.lockは白紙)
source "https://rubygems.org"
gem "rails", "7.1.3.4"

## 初回起動後ローカルPCで実行
docker cp main-container-ID:/railsapp ./main
