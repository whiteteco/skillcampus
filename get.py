from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)


# SQLiteデータベースからデータを取得する関数
def get_locations_from_db():
    conn = sqlite3.connect("skillcampus.db")  # データベースに接続
    cursor = conn.cursor()

    # 場所名、緯度、経度を取得
    cursor.execute("SELECT name, lat, lng FROM locations")
    locations = cursor.fetchall()

    conn.close()
    return locations


@app.route("/get_locations", methods=["GET"])
def get_locations():
    locations = get_locations_from_db()
    return jsonify(locations)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
