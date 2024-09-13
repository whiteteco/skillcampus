from flask import Flask, jsonify, render_template
from peewee import SqliteDatabase, Model, IntegerField, CharField, DecimalField

# Flask アプリケーション
app = Flask(__name__)

# SQLiteデータベース接続設定
db = SqliteDatabase("peewee_db_sqlite")


# sc_map テーブルのモデル定義
class SCMap(Model):
    id = IntegerField()
    name = CharField()
    lat = DecimalField()
    lng = DecimalField()
    category = CharField()
    capacity = IntegerField()

    class Meta:
        database = db  # データベースを指定


# データベース接続
db.connect()


# データベースからデータを取得する関数
def get_map_data():
    # sc_map テーブルからすべてのレコードを取得
    query = SCMap.select()

    # データをリスト形式に変換
    data = []
    for record in query:
        data.append(
            {
                "id": record.id,
                "name": record.name,
                "lat": record.lat,
                "lng": record.lng,
                "category": record.category,
                "capacity": record.capacity,
            }
        )

    return data


# 地図データを返すAPIエンドポイント
@app.route("/map-data")
def map_data():
    data = get_map_data()
    return jsonify(data)


# index.html を表示するルート
@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
