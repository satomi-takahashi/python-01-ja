# セットアップと実行の手順
  
#### 1. Pythonのインストール：  
公式のウェブサイト<https://www.python.org/downloads/> から最新バージョンの Python をダウンロードしてインストールできます。


#### 2. IDEのインストール：  
例として、Visual Studio Code（VS Code）公式のウェブサイトから<https://code.visualstudio.com/>から  
お使いのオペレーティングシステムに合ったバージョンをダウンロードしてインストールできます。

#### 3. main.py を起動させてください。



# プロジェクトにおける重要な設計やその設計理由

#### このアプリーションは、書籍の既読未読を管理するためのデジタルブックシェルフです。  
登録に必要な項目は、以下の通りです。

**[book_id]**  
本のID（半角数字）※book idは固定ではありません。1以上で自動的に割り当てされ、一つの本が削除されると後ろのbook id が繰り上がります。

**[title]**  
本のタイトル（半角全角いずれも入力可）

**[read_status]**  
既読未読の状況（既読＝”yes” / 未読＝”no”：半角英字で入力）

タイトルは日本語入力もできますが、それ以外の質問項目の入力はすべて半角英数で入力してください。
意図しない値が入力された場合、再入力を促します。指定された入力形式で再入力すると進めます。



# このツールまたはサービスの使い方の説明

#### 1. 起動時にメニュー画面が表示されるので、1-6の半角数字を入力してください 
 
    Welcome to your personal books digital library!

    1: Add a Book  
    2: Edit a Book  
    3: Search for Books  
    4: Delete a Book  
    5: View Library Stats  
    6: Exit App  

    Please select from 1 to 6 : 

#### 2. メニューの詳細

**1: Add a Book（本の登録）**  
使い始めるには、まず本のデータを登録してください。
登録に必要な項目は、title もしくは read statusです。

**2: Edit a Book（編集）**  
編集したいbook idを指定して、タイトルもしくは既読/未読の状況を編集できます。
本が削除されるとbook idが繰り上がるため、3．Search for books で最新のbook idを確認して入力してください
book idは自動可変のため、ユーザーは編集できません。

**3: Search for Books（検索）**  
既存データを検索します。検索キーは、title もしくは read statusです。
book idをキーとして検索することはできません。

**4: Delete a Book（削除）**    
一回の動作で削除できるのは1冊のみです。
既存データからbook idをキーとしてデータを削除します。
メニュー画面の「3. Search for book」で最新のbook id を確認してから実行してください。
book id を入力すると、対象データが表示されますので内容を確認してください。
対象のデータが削除されると、後ろのデータのbook idが繰り上がります。

**5: View Library Stats（統計の表示）**  
以下のようにライブラリーの統計を表示します。
  
    [Library Stats]  
    Total number of books: 0　（本棚に登録された総数）  
    Number of read books: 0　　（既読の数）  
    Number of unread books: 0　（未読の数）  

**6: Exit App（終了）**  
アプリケーションを終了します。
