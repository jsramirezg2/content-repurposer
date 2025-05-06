from flask import Flask, render_template, jsonify, request, redirect, url_for
from services.processor import repurpose_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        content = request.form.get("content")
        platform = request.form.get("platform")
        if content and platform:
            result = repurpose_text(content, platform)
            return redirect(url_for("result", result=result))
    return render_template("index.html")

@app.route("/result")
def result():
    result = request.args.get("result", None)
    return render_template("result.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)