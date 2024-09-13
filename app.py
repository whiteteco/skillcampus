from flask import Flask, render_template
from peewee import SqliteDatabase, Model, DecimalField, CharField

app = Flask(__name__)

# SQLiteデータベースの接続
db = SqliteDatabase("peewee_db.sqlite")


# Mapモデルの定義
class Map(Model):
    name = CharField()  # マーカーの名前
    lat = DecimalField()  # 緯度
    lng = DecimalField()  # 経度
    url = CharField()  # マーカーの画像URL
    category = CharField()  # カテゴリ (例: school, hotel, food)

    class Meta:
        database = db


# ルートURLにアクセスした時の処理
@app.route("/")
def index():
    # カテゴリごとにデータを取得
    school = Map.select().where(Map.category == "school")
    hotel = Map.select().where(Map.category == "hotel")
    food = Map.select().where(Map.category == "food")

    # すべてのマーカー情報をリスト形式に変換
    markers = list(Map.select().dicts())

    # カテゴリごとのリストとマーカーリストをテンプレートに渡す
    return render_template("index.html", school=school, hotel=hotel, food=food, markers=markers)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
