# README

## Windows(Python3インストール済)におけるアプリの起動方法

1 コマンドプロンプトを選択

2 cd FlaskMarket (ディレクトリに設定)

3 python -m venv venv (初回の仮想環境作成時のみ)

4 .\venv\Scripts\activate (仮想環境の有効化)

5 pip install -r ./config/requirements.txt (ライブラリのインストール時のみ)

6 pip freeze > ./config/requirements.txt (インストールしたものを記載)

7 python run.py (簡易WEBサーバーの起動)

8 CTRL + C (サーバーの停止)

9 pytest test.py (自動テストの実行時のみ)

10 set FLASK_APP=coreApp (マイグレーション前に環境変数を設定)

11 flask db init (初回マイグレーションの直前のみ)

12 flask db migrate (マイグレーションの実行時のみ)

13 deactivate (仮想環境の無効化)
