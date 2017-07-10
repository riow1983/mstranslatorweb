# mstranslatorweb
#Microsoft Translator APIを組み入れた翻訳Webアプリケーションを作成しました。


##手順１：Microsoft Azureでサブスクリプションを購入（無料）
Microsoftアカウントを取得後、Azureのページに行けば何やかんや言われた通りにする。

##手順２：サブスクリプションの中にTranslator API（２００万文字/月まで無料）を導入
サブスクリプションのページから追加したいライブラリを選択して追加する。検索欄に"Microsoft Translator API"を入れるとCognitive Serviceの分類中からMicrosoft Translator APIを選択する画面に飛ぶので追加する。
なお、手順１〜手順２の途中でクレジットカード情報を入れる必要がある。無料だけど入れる必要あり。ここは思い切って入力しましょう。でないと先に進めません。

##手順３：mstranslatorをインストール
PythonからTranslator APIを動かせるライブラリが無いか物色。
https://pypi.python.org/pypi/mstranslator
これがPython3からでも動かせる良いライブラリの予感。
$ pip install mstranslator
で落としましょう。

##動作確認作業：mstranslatorがちゃんと動くか検証
```Python
>>>from mstranslator import Translator
>>>translator = Translator("YOUR_ACCESS_KEY")
>>>original = "今朝の朝食はとんかつでした。"
>>>translator.translate(original, lang_from='ja', lang_to='en')
>>>'Breakfast this morning was the tonkatsu.'
```
うん、ちゃんと動いているようです。


##手順４：実装（当レポジトリの内容）
入力フォームに日本語か英語を入力し、翻訳ボタンを押すと翻訳文が表示され、と同時にDBに翻訳前文と翻訳文がセットで保存されるという仕組みのWebアプリケーションを作成しました。詳細はコードを確認してください。

##完成
Webブラウザ上でもちゃんと動くことが確認されました。後は翻訳文の文字サイズの拡大などインターフェースの改良が必要です。それからiOSアプリ,Androidアプリとして提供されているMicrosoft Translatorと当APIの翻訳精度の比較をして見ましたが、残念ながらAPIのほうが精度が劣ります。この精度の違いについては日本マイクロソフトの営業担当の人に直接問い合わせております。