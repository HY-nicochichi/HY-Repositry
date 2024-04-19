FROM ruby:3.2.3-slim-bookworm

RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs

COPY . /
WORKDIR /railsapp

RUN bundle install

CMD ["sh", "/cmd.sh"]
