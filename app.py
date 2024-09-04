from flask import Flask, render_template
import os
from dotenv import load_dotenv

load_dotenv()  # .envファイルの内容を読み込む

app = Flask(__name__)


@app.route("/")
def map():
    google_maps_api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    return render_template("index.html", api_key=google_maps_api_key)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
