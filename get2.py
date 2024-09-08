from flask import Flask, jsonify, render_template
from peewee import SqliteDatabase, Model, IntegerField, CharField, CharField

# Flask アプリケーション
app = Flask(__name__)

# SQLiteデータベース接続設定
db = SqliteDatabase("peewee_db_sqlite")


# sc_maker テーブルのモデル定義
class SCMaker(Model):
    id = IntegerField()
    category = CharField()
    url = CharField()

    class Meta:
        database = db  # データベースを指定


# データベース接続
db.connect()


# データベースからデータを取得する関数
def get_maker_data():
    # sc_maker テーブルからすべてのレコードを取得
    query = SCMaker.select()

    # データをリスト形式に変換
    data = []
    for record in query:
        data.append(
            {
                "id": record.id,
                "category": record.category,
                "url": record.url,
            }
        )

    return data


# 地図データを返すAPIエンドポイント
@app.route("/maker-data")
def maker_data():
    data = get_maker_data()
    return jsonify(data)


# index.html を表示するルート
@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=8000, debug=True)
