# Blogzart!

## 説明

**Blogzart!** は使いやすさと豊かな機能性を重視したFlaskベースの包括的なブログプラットフォームです。コンテンツクリエイターにとって創造的なアウトレットを提供し、読者が投稿と交流するインタラクティブな空間を提供します。

## 特徴

### 現在の特徴
- **ユーザー認証**: ユーザーアカウントを管理するための堅牢なサインアップおよびログイン機能。
- **いいねシステム**: ユーザーは投稿にいいねをすることでコンテンツに対する感謝を示すことができます。
- **コメントシステム**: ブログ投稿にコメントすることでコミュニティと交流します。
- **リッチテキストエディタ**: CKEditorを利用して、詳細なコンテンツ作成を可能にします。
- **レスポンシブデザイン**: Flask-Bootstrapを使用して、あらゆるデバイスでスムーズな体験を保証します。
- **Gravatar統合**: 個性的なユーザーアバターを表示します。
- **メール統合**: ユーザー間のやり取りや通知のためのメール操作をサポートします。
- **管理者ダッシュボード**: サイト管理者が投稿やユーザーを効果的に管理するための装備。

### 今後の拡張機能

- **AIベースのコメントモデレーション**: GCPにホストされたLSTM RNNモデルは、RenderにホストされたメインブログプラットフォームからのRESTful APIコールを通じて、リアルタイムでコメントをモデレートします。この統合により、99％の精度率で効率的かつスケーラブルなコメントモデレーションが保証されます。
- **こちらがリポジトリです**: [ここをクリック](https://github.com/rakibulhaque9954/Comment_Flag_LSTM_Model.git)

## Blogzart 2.0の新機能

- **クラウドパワーAIモデレーション**: Blogzartは現在、GCPにデプロイされたLSTMベースのフラッガーを活用して、クラウドコンピューティングの力を活用しています。これにより、コメント提出への高可用性と低遅延応答が可能になります。
- **RESTful API統合**: プラットフォームは、RenderにホストされたメインブログからのRESTful APIリクエストを使用してコメント分析を行い、ユーザーにシームレスな体験を提供し、議論の整合性を保ちます。
- **スケーラブルなアーキテクチャ**: AIモデルをホストするためにGCPを使用することで、Blogzartはトラフィックとコメントの量が増加してもパフォーマンスを損なうことなく対応できます。

## GCPにデプロイ

BlogzartのAIモデレーションシステムはFlaskで構築され、Google Cloud Platformにホストされており、その管理サービスを活用して高いパフォーマンスと可用性を保証します。RESTful APIは、RenderにホストされたメインブログとAIモデルとのシームレスな通信を可能にし、クラウドにコメント分析の重い処理をオフロードします。このアプローチにより、プラットフォームの成長に伴ってもユーザー体験が迅速かつ応答性に優れたままでいることが保証されます。

![毒性コメント](https://github.com/rakibulhaque9954/blog_remastered/blob/adc3cb260e2fc032a888f194fe0fc02e048dda5e/comment.png)
*毒性コメント*

![フラッグ付きメッセージ](https://github.com/rakibulhaque9954/blog_remastered/blob/adc3cb260e2fc032a888f194fe0fc02e048dda5e/flagged%20message.png)
*フラッグ付きメッセージ*

Blogzart体験をさらに向上させるためのアップデートをお楽しみに！

## はじめに

### 前提条件
マシンにPython 3.6以上とpipがインストールされていることを確認してください。

### インストール

```bash
# Blogzart! リポジトリをクローンします
git clone https://github.com/rakibulhaque9954/blog_remastered

# プロジェクトディレクトリに移動します
cd path-to-Blogzart

# 必要な依存関係をインストールします
pip install -r requirements.txt

# 環境変数を設定します
export MY_EMAIL='your-email@example.com'
export APP_PASSWORD='your-email-app-password'
export SECRET_KEY='your-secret-key'

# データベースの初期化
flask db init
flask db migrate
flask db upgrade

# サーバーを起動します
flask run
```
ブラウザで http://localhost:5000 にアクセスしてBlogzart!を始めてください！

## コードベース概要

### server.py
アプリケーションのバックボーンとして機能し、サーバーの設定、ルートの設定、Flask拡張機能の統合を行います。

### index_try.html
ユーザー認証に基づいて異なるコンテンツを表示するロジックを組み込み、コメントやいいねなどの動的コンテンツのエリアを提供するメインランディングページテンプレートとして機能します。

## ライセンス

このプロジェクトはMITライセンスの下でライセンスされています - 詳細は[LICENSE](https://github.com/rakibulhaque9954/blog_remastered/blob/2067516a1ceb3aff915fc2cd47be07df46cf7bb6/MIT_LICENSE_Rakibul_Haque.txt)ファイルを参照してください。

## お問い合わせ

Blogzart!に関するご質問やフィードバックがある場合は、GitHubリポジトリで問題を開いてください。

## 謝辞

Blogzart!を形作るのに役立ったすべてのオープンソースの貢献者とコミュニティに深い感謝を表します。
