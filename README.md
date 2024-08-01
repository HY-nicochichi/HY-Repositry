# HY-Repositry

## GCP_Projects
Google Cloud Platform へのデプロイ用に作ったプロジェクトをまとめたもの。　詳細はGCP_projects/README.mdに記載。

## SPA-and-API
Vue(フロントエンド)とFlask(バックエンド)で作ったWEBサイト(ユーザー認証機能のみ実装)。　VueはCDN版ではなくNode.jsを用いたSPAであり(デザインはCDN版Bootstrap)、Flaskは認証API(JWT, CORS, O/Rマッパー, セキュリティヘッダ, モジュール分割)、という仕様になっている。　起動後にブラウザでアクセス ⇒ http://localhost:8080

## RailsApp01
Railsの勉強のためにお試しで作ったブログアプリ。　Windows上で動かしMySQLと連携している。　起動後にブラウザでアクセス ⇒ http://localhost:3000

## RailsApp02
Railsをガチで学ぶためのアプリ(ユーザー認証機能のみ実装)。　Railsチュートリアルをベースにして作成しつつ、少し個性を出している(DBによるセッション管理やCDN版Bootstrapなど)。　動作環境は、初めは01と全く同じWindows＆MySQLだったが、後にDocker＆PostgrSQLに移植した。　起動後にブラウザでアクセス ⇒ http://localhost:3000

## ReadEN
初めて作ったAndroidアプリ("Kotlin ＋ Android Studio"を使用)。　英語の５文型を当てるクイズアプリ。
