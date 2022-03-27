# SQL Injection demo using SQLite

SQLiteを使ってSQLインジェクションのデモを行います。

> 推奨動作環境: python3 (標準ライブラリのみ使用)

最初に`init.py`を使ってデータベースを初期化します。

その後、`get_sql_only.py`でSQL文の動作を確認したあと、`get_normal_placeholder.py`で検索処理の例を実行します。このファイルでは通常のクエリとして、"taro"という名前のユーザーを検索するようにしています。

`get_injected_placeholder.py`では、さきほどの`get_normal_placeholder.py`で"taro"という名前のユーザーを検索したのに対し、検索窓に不正なクエリを挿入されたことを想定するものになっています。