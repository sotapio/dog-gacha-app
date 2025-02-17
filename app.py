from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

# ランダムな犬の画像を取得するAPI
@app.route('/random-dog')
def get_dog():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    if response.status_code == 200:
        return jsonify(response.json())  # JSONをそのまま返す
    else:
        return jsonify({"message": "エラーが発生しました"}), 500

# 指定した犬種の画像を取得するAPI
@app.route('/random-dog/<breed>')
def get_dog_by_breed(breed):
    response = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random")
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"message": "犬種が見つかりません"}), 404

# HTMLを表示するルート
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
