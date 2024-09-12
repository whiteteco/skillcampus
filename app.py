from flask import Flask, render_template, jsonify
from peewee import SqliteDatabase, Model, FloatField, TextField

app = Flask(__name__)

# SQLiteデータベースの設定
db = SqliteDatabase("peewee_db.sqlite")


# sc_mapモデルの定義
class Map(Model):
    lat = FloatField()
    lng = FloatField()
    name = TextField()
    category = TextField()  # カテゴリ列を追加

    class Meta:
        database = db
        db_table = "sc_map"  # テーブル名を指定


# sc_makerモデルの定義
class Marker(Model):
    icon_url = TextField()  # マーカーの画像URL
    category = TextField()  # カテゴリ（school, hotel, foodなど）

    class Meta:
        database = db
        db_table = "sc_maker"  # テーブル名を指定


# カテゴリごとのデータを取得して表示
@app.route("/")
def index():
    school = Map.select().where(Map.category == "school")
    hotel = Map.select().where(Map.category == "hotel")
    food = Map.select().where(Map.category == "food")

    # カテゴリごとのリストをテンプレートに渡す
    return render_template("index.html", school=school, hotel=hotel, food=food)


# マーカー情報を取得するAPI
@app.route("/markers")
def get_markers():
    # sc_mapテーブルから位置情報を取得し、sc_makerテーブルから対応するマーカーURLを取得
    markers = Map.select(Map.lat, Map.lng, Map.name, Marker.icon_url).join(
        Marker, on=(Map.category == Marker.category)
    )  # カテゴリで結合

    markers_list = [
        {"lat": marker.lat, "lng": marker.lng, "name": marker.name, "icon": marker.icon_url}
        for marker in markers
    ]
    return jsonify(markers_list)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
