# Django Pair Programming Project

共同開発のための環境構築手順です。

## 必要なもの
1. Docker Desktop: https://www.docker.com/products/docker-desktop/
2. GitHubアカウント

## セットアップ手順
1. Docker Desktopをインストールして起動

2. プロジェクトのクローン
git clone https://github.com/nisyy/django-pair-project
cd django-pair-project

3. コンテナのビルドと起動
bashCopydocker compose up --build

4.ブラウザで確認
http://localhost:8000 にアクセス


dockerの開発の開始と終了コマンド  
docker compose up   
docker compose down  
