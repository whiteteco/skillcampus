from flask import Flask, render_template, jsonify
from peewee import SqliteDatabase, Model, FloatField, TextField

app = Flask(__name__)

# SQLiteデータベースの設定
db = SqliteDatabase("peewee_db.sqlite")


# sc_mapモデルの定義
class Sc_Map(Model):
    lat = FloatField()
    lng = FloatField()
    name = TextField()
    category = TextField()  # カテゴリ列を追加

    class Meta:
        database = db


# カテゴリごとのデータを取得
@app.route("/")
def index():
    school = Sc_Map.select().where(Sc_Map.category == "school")
    hotel = Sc_Map.select().where(Sc_Map.category == "hotel")
    food = Sc_Map.select().where(Sc_Map.category == "food")

    # カテゴリごとのリストをテンプレートに渡す
    return render_template("index.html", school=school, hotel=hotel, food=food)


# マーカー情報を取得するAPI
@app.route("/markers")
def get_markers():
    markers = Sc_Map.select()
    markers_list = [{"lat": marker.lat, "lng": marker.lng, "name": marker.name} for marker in markers]
    return jsonify(markers_list)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
