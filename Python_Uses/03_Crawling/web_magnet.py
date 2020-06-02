from flask import Flask
from flask import render_template
from flask import request
from magnet_module import search_google

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])  # GET방식과 POST 방식 모두 사용한다
def index():
    if "keyword" in request.form:  # 전송한 form으로 부터 키워드 받는다
        keyword = request.form["keyword"]
        results = search_google(keyword, 0)
    else:
        results = []

    if len(results) > 0:
        # 검색결과인 results 딕셔너리 형태로 넘겨준다(kwargs)
        return render_template("index.html", **{"magnets": results})
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9995, debug=True)
