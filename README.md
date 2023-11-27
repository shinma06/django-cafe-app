# CafeApp

## 概要
CafeAppは、架空のカフェのウェブアプリケーションです。DjangoとMySQLを使用し、Dockerを利用して環境を構築しました。このプロジェクトは、学習目的で作成しました。

## 機能説明
CafeAppでは、従業員側とユーザー側の機能が分けられています。

### 従業員側の機能
- メニュー管理: 従業員はメニュー項目の追加、編集、削除が可能です。
- 予約管理: カフェの予約状況を確認することができます。
- ニュース投稿: カフェのニュースやイベント情報を投稿、編集。削除できます。
- お問い合わせ対応: ユーザーからのお問い合わせメールを受信し、管理できます。

### ユーザー側の機能
- メニュー閲覧: カフェのメニューを閲覧できます。
- オンライン予約: カフェのテーブルをオンラインで予約できます。
- ニュース閲覧: カフェの最新ニュースをカテゴリごとに絞り込んで確認できます。
- お問い合わせ: カフェへのお問い合わせをメールで送信できます。
- アカウント: アカウントの作成、ログイン、ログアウト、ユーザー名の変更ができます。

※リポジトリからインストールして使用する場合メール機能は使用できません。

## 現在のステータス
現在、メニュー詳細ページの追加を計画しています。このページでは、メニューの詳細説明の閲覧やレビューを行うことができます。
しかし、フロントエンドの開発スキルが不足しているため、この新機能の追加は一時中断されています。

## 技術スタック
- Python 3.11.4
- Django 4.2.4
- MySQL 8.1.0
- Docker (最新版を推奨)
- Gmail API

### Pythonライブラリは requirements.txt を参照

## インストール方法

```

git clone https://github.com/shinma06/cafeapp
cd cafeapp
docker-compose build
docker-compose up -d

```


## 使用方法
アプリケーションは http://localhost:8000 でアクセス可能です。

## 管理者アカウントの作成

1. 稼働中のコンテナを確認

まずは docker ps コマンドを使って、現在稼働中のコンテナの状態を確認します。

`docker ps`

出力例：

```

CONTAINER ID   IMAGE         COMMAND                   CREATED      STATUS          PORTS                               NAMES
xxxxxxxxxxxx   cafeapp-web   "./combined_script.sh"    x days ago   Up x minutes   0.0.0.0:8000->8000/tcp              cafeapp-web-1
xxxxxxxxxxxx   mysql:8.1.0   "docker-entrypoint.s…"   x days ago   Up x minutes   0.0.0.0:3306->3306/tcp, 33060/tcp   mysql

```

2. Django のスーパーユーザーを作成

CafeApp のコンテナ内で Django のスーパーユーザーを作成するために、以下のコマンドを実行します。ここで XXX は docker ps コマンドの出力で表示された cafeapp-web コンテナの CONTAINER ID の頭文字2～3文字に置き換えてください。

`docker exec -it xxx bash`

次に、Django のスーパーユーザーを作成します。

`python manage.py createsuperuser`

以下の手順でユーザー情報を入力します：

ユーザー名：任意のユーザー名を入力して Enter。
メールアドレス：何も入力せず Enter。
パスワード：任意のパスワードを入力して Enter。簡単なもので構いません。
パスワード（再入力）：先ほど入力したパスワードを再度入力して Enter。
パスワードの複雑性に関する警告が表示される場合：

警告が表示された場合は、y を入力して Enter。これでスーパーユーザーが作成されます。
成功すると、「Superuser created successfully.」と表示されます。
作成したユーザー名とパスワードでログインすることで従業員用の機能が使用できるようになります。

## 参考文献・ウェブサイト

### 書籍
[1冊ですべて身につくHTML & CSSとWebデザイン入門講座: ](https://www.sbcr.jp/product/4797398892/)
この書籍は、HTMLとCSSに関する基本的な概念と実践的なコーディング技術を紹介しています。

### ウェブサイト
[ページネーションデザイン: ](https://eclair.blog/example-of-pagination/)
このサイトは、コピペですぐに導入できるシンプルで汎用的なページネーションデザインのアイデアを提供しています。

## 開発の動機と学び
このプロジェクトを通じて、Djangoの基本、データベースとの連携、Dockerを使用した環境構築などのスキルを学習しました。