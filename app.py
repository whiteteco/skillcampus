from flask import Flask, render_template, request, jsonify
from peewee import *

# Flaskアプリケーションの作成
app = Flask(__name__)

# SQLiteデータベース接続
db = SqliteDatabase('peewee_db.sqlite')

# モデル定義
class Map(Model):
    name = CharField()
    lat = DecimalField()
    lng = DecimalField()
    capacity = IntegerField()
    url = CharField()

    class Meta:
        database = db

# ルートハンドラー
@app.route('/')
def index():
    return render_template('index.html')

# /get_markers エンドポイント
# フロントエンドから送られてきたcapacityに基づいて、該当するマーカーを返す
@app.route('/get_markers', methods=['GET'])
def get_markers():
    # capacity パラメータを取得し、デフォルトで0を使用
    min_capacity = request.args.get('capacity', 0, type=int)
    
    # capacity >= min_capacityの条件に合うマーカーを取得
    markers = Map.select().where(Map.capacity >= min_capacity)
    
    # マーカー情報をリストに変換
    marker_data = [{
        'name': marker.name,
        'lat': float(marker.lat),  # DecimalFieldをfloatに変換
        'lng': float(marker.lng),
        'capacity': marker.capacity,
        'url': marker.url
    } for marker in markers]

    # デバッグ用：取得されたマーカーをサーバーのコンソールに表示
    print("Markers fetched for capacity {}:".format(min_capacity), marker_data)

    # マーカー情報をJSON形式で返す
    return jsonify(marker_data)

# アプリケーションの起動
if __name__ == '__main__':
    app.run(port=8000, debug=True)
