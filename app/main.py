from flask import Flask, render_template, jsonify, request
from services.processor import repurpose_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        content = request.form.get("content")
        platform = request.form.get("platform")
        if content and platform:
            result = repurpose_text(content, platform)
    return render_template("index.html", result=result)
if __name__ == '__main__':
    app.run(debug=True)