# HY-Repositry

## GCP_Projects
Google Cloud Platform へのデプロイ用に作ったプロジェクトをまとめたもの。　詳細はGCP_projects/README.mdに記載。

## SPA-and-API
Vue(フロントエンド)とFlask(バックエンド)で作ったWEBサイト(ユーザー認証機能のみ実装)。　VueはSPAであり(OptionAPI & JS -> CompositionAPI & TS, デザインはCDN版Bootstrap, モバイルアプリの画面としても利用できるように工夫済み)、Flaskは認証API(JWT, CORS, O/Rマッパー, モジュール分割)、という仕様になっている。　起動後にブラウザでアクセス ⇒ http://localhost:8080

## RailsAPI
SPA-and-APIと同じ構造のWEBサイトを、バックエンドをRailsに置き換えて作ったもの。　Vueは旧来のOptionAPIではなく最新のCompositionAPI(script setup)で作成し、Railsの認証APIはFlaskと同じくCORSやJWTなどの機能を使用している。　起動後にブラウザでアクセス ⇒ http://localhost:8080

## ReadEN
初めて作った簡素なAndroid用ネイティブアプリ("Kotlin ＋ Android Studio"を使用)。　英語の５文型を当てるクイズアプリ。

## SPA-and-API Android
SPA-and-APIのAndroidアプリ版("Kotlin ＋ Android Studio"を使用)。　WebViewを使用し、SPA-and-APIのサイトをアプリ内で表示する、という方法で制作。

## FlaskMDM
Android Management API を利用した簡単なMDMアプリ。　現時点ではバックエンドAPI(Flask)のみを実装済み。
