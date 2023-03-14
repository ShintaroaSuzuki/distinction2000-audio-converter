# distinction2000-audio-converter

## 概要

[『Distinction 2000』ATSU](https://www.kadokawa.co.jp/product/321907000333/) のダウンロード音声ファイルを自己学習用に変換するスクリプトです。

入力に用いる音声データは下記の URL からダウンロードしています。

[https://app.abceed.com/libraries/detail/kadokawa_distinction_2000/voice](https://app.abceed.com/libraries/detail/kadokawa_distinction_2000/voice)

[abceed](https://www.abceed.com) への登録が必要です。

## 環境構築

```
$ brew install ffmpeg
$ pip install pipenv
$ pipenv sync --dev
```

## 使い方

```
$ pipenv run convert ~/Music/audio ~/Music/distinction2000_natural
```
