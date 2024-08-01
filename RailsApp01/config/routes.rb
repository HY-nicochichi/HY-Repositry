Rails.application.routes.draw do

    # TOPページ
    get "/", to: "index#index"

    # ユーザー管理系
    get "/login", to: "auth#login"       # ログイン
    post "/login", to: "auth#login_post"
    get "/logout", to: "auth#logout"     # ログアウト
    get "/signin", to: "auth#signin"     # アカウント登録
    post "/signin", to: "auth#signin_post"
    get "/signout", to: "auth#signout"   # アカウント削除

    # ブログ管理系
    get "/articles", to: "blog#articles"     # 記事一覧
    get "/new_article", to: "blog#new_article"       # 記事投稿
    post "/new_article", to: "blog#new_article_post"
    get "/edit_article", to: "blog#edit_article"     # 記事編集
    post "/edit_article", to: "blog#edit_article_post"
    get "/delete_article", to: "blog#delete_article"   # 記事削除

end
