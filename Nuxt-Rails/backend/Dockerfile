FROM ruby:3.3.4-slim-bookworm

RUN apt-get update -qq && apt-get install -y build-essential libpq-dev

COPY . /
WORKDIR /railsapi

RUN bundle install

CMD ["sh", "/cmd.sh"]
