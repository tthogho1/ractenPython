# Pinecone Aassistant with Rakuten Hotel Search Data

Rakutenのホテル検索データをPinecone Aassistantに登録するバッチプログラムと、登録したデータをもとにPinecone AassistantとチャットするFlaskサーバを提供します。

## バッチプログラムの実行

Rakutenのホテル検索からデータファイルを作成するバッチ
このプログラムは、Rakuten APIからデータを取得し、ホテルごとにテキストファイルを作成する
```bash
python registEmbedding.py
```

作成したテキストファイルを結合して一つのファイルにするバッチ。
結合したファイルをPincone assistantにアップロードする。


```bash
python fileCombiner.py
```

## Flaskサーバの起動
Pincone assistantの設定が完了したのち、Flaskサーバを起動する。
Flaskサーバを起動するには、以下のコマンドを実行します。

```bash
python app.py
```

サーバが起動したら、ブラウザで `http://127.0.0.1:5000` にアクセスして、Pinecone Aassistantとチャットを開始できます。

## 使用方法

1. ブラウザでFlaskサーバにアクセスします。
2. チャットボックスに質問を入力し、送信します。
3. Pinecone AassistantがRakutenのホテルデータをもとに応答します。

## 注意事項

- Rakuten APIの使用にはAPIキーが必要です。事前に取得してください。
- Pineconeのアカウントを作成し、APIキーを取得する必要があります。

