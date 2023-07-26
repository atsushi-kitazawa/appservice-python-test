import os
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    print(os.environ)
    return os.getenv('KEY3')

## 実行
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)