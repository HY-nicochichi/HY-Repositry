class BlogController < ActionController::Base

    # 記事一覧
    def articles
        if session[:user]
            @articles = Article.all
            @user = session[:user]
        else
            redirect_to("/login")
        end
    end

    # 記事投稿
    def new_article
        unless session[:user]
            redirect_to("/login")
        end
    end

    def new_article_post
        if session[:user]
            title = params[:title]
            body = params[:body]
            user = session[:user]
            Article.create(title: title, body: body, user: user)
            redirect_to("/articles")
        else
            redirect_to("/login")
        end
    end


    # 記事編集
    def edit_article
        if session[:user] && Article.find_by(id: params[:id]).user == session[:user]
            @article = Article.find_by(id: params[:id])
        else
            redirect_to("/login")
        end
    end

    def edit_article_post
        if session[:user]
            id = params[:id]
            title = params[:title]
            body = params[:body]
            article = Article.find_by(id: id)
            article.update(title: title, body: body)
            redirect_to("/articles")
        else
            redirect_to("/login")
        end
    end

    # 記事削除
    def delete_article
        if session[:user] && Article.find_by(id: params[:id]).user == session[:user]
            Article.find_by(id: params[:id]).destroy
            redirect_to("/articles")
        else
            redirect_to("/login")
        end
    end

end
