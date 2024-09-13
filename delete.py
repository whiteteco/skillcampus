import sqlite3

# データベース読み込み
db = sqlite3.connect(
    "peewee_db.sqlite",  # ファイル名
    isolation_level=None,
)

# Kudamonoテーブルを削除
sql = """DROP TABLE map"""

db.execute(sql)  # sql文を実行
db.close()  # データベースを閉じる
