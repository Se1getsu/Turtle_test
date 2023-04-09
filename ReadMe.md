# turtle-test
2023年の新歓で行った「プログラミング初心者講座」のために作成した資料です。

# Content
- [`test01`](./test01.py) :
`turtle` の関数を公式ドキュメントを見ながらまとめたものです。
10項目に分けてるので、実行時には動作を確認したい項目(`option`)の番号を入力します。
- [`test02`](./test02.py) :
講座で扱うコードの一覧です。10段階に分けています。

# Manual
以下に、新歓用の「プログラミング初心者講座」の手順を記します。

目安時間は 1 ~ 1.5 時間 程度で、途中でやめてもOK。
教える側は VSCode と Python が少しでも分かれば問題ないです。
[`test01`](./test01.py) は、軽く目を通しておくか、最悪読まなくてもいいです。

0. まず、「プログラミング初心者講座」に受講する新入生（以降、**体験者**と呼ぶ）のPCと、教える人のPCを並べます。新入生がPCを持ってない場合、部室の適当なPCを使用します。

1. 体験者のPCにVSCodeとPythonをインストールします。
環境変数どうこうとかはないので簡単にできるはずです。
Pythonは公式サイトからinstallerをダウンロードしてください。
体験者のPCが32bitか64bitか分からない時は、 `Ctrl-X` > \[システム] で確認できます。

2. デスクトップに適当にフォルダを作らせ、VSCodeにドラッグして開きます。

3. VSCodeで`適当なファイル名.py`を作成し、`print("Hello, world")`と入力して、`Ctrl-S`で保存して、`Ctrl-Shift-@` (Macも`Command`ではなく`Ctrl`) でターミナルを開き、`py ファイル名.py`で実行します。

4. [`test02`](./test02.py)をカンペにして「説明しながら書いて、体験者に写させ、実行」を`stage=1`から`stage=10`まで繰り返します。次の`stage`に進む時、前の`stage`のコードは残さなくていいです。

5. 最後まで終わって体験者に時間的余裕があれば、やりたいようにやらせて慣れさせたり、プログラミングのどういう分野に興味があるのか、情報を与えたり引き出したりして適切な助言を行ったりします。

講座は以上で終了です。