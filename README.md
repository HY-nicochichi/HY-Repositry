# HY-Repositry

## GCP_Projects
Google Cloud Platform へのデプロイ用に作ったプロジェクトをまとめたもの。　詳細はGCP_projects/README.mdに記載。

## SPA-and-API
Vue(フロントエンド)とFlask(バックエンド)で作ったWEBサイト(ユーザー認証機能のみ実装)。　VueはCDN版ではなくSPAであり(OptionAPI, デザインはCDN版Bootstrap)、Flaskは認証API(JWT, CORS, O/Rマッパー, セキュリティヘッダ, モジュール分割)、という仕様になっている。　起動後にブラウザでアクセス ⇒ http://localhost:8080

## RailsAPI
SPA-and-APIと同じ構造のWEBサイトを、バックエンドをRailsに置き換えて作ったもの。　Vueはこちらでは旧来のOptionAPIではなく最新のCompositionAPI(script setup)で作成し、Railsの認証APIはFlaskと同じくCORSやJWTなどの機能を使用している。　起動後にブラウザでアクセス ⇒ http://localhost:8080

## ReadEN
初めて作った簡素なAndroid用ネイティブアプリ("Kotlin ＋ Android Studio"を使用)。　英語の５文型を当てるクイズアプリ。

## FlaskMDM
Android Management API を利用した簡単なMDMサービス。　現時点ではバックエンドAPI(Flask)のみを実装済み。
