# FSEC plotter

島津 Fluorescence-Detection Size-Exclusion Chromatographyのアウトプットデータ(テキストファイル)から
作図を行うためのプログラムです。

# すぐに実行するには

すぐに実行するためには`FSEC plotter.exe`をのみをダウンロードしてダブルクリックで実行してください。
ダウンロード手順は下記のとおりです。

- [こちら](https://github.com/toasty-kj/FSECplot/blob/develop/FSEC%20plotter.exe)画面に遷移
- 右上の三点リーダー(・・・)をクリックする
- ダウンロードをクリックする
- ダウンロードした`FSEC plotter.exe`を実行する

# プログラムを編集するには

下記手順はFSEC plotterのプログラムを編集する際に必要な手順です。編集が必要な場合は実施不要です。

0. 初期段階
   下記についてはすでに行われている前提で手順を記載します。(されていない場合は先にこちらを実施してから後続の手順を行ってください)

   - githubのアカウント作成
   - git bashのインストール

1. git レポジトリのクローン

```bash
git clone https://github.com/toasty-kj/FSECplot.git
```

2. cloneしたリポジトリへ移動

```bash
cd FSECplot
```

3. パッケージのインストール
```bash
npm ci
```

4. このプログラムを動かすにあたってpythonのライブラリであるmatplotlibをインストールする必要があります。  
コマンドラインから以下のコマンドを入力することでインストールできます。

```python:title
pip install matplotlib
```

~~次に以下のようにしてzip fileでファイルをダウンロード、解凍してください。~~
![image](https://user-images.githubusercontent.com/74779681/209974374-04ca32b4-c8c6-48d3-9deb-0b7fc10a2ab5.png)~

ランする際はのFSEC plotter.exeをダブルクリックで起動してください。
