from flask import Flask, render_template, jsonify, request, redirect, url_for
from services.processor import repurpose_text_input
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        input_type = request.form.get("input_type")
        platform = request.form.get("platform")

        if input_type == "text":
            content = request.form.get("content")
            if content and platform:
                result = repurpose_text_input(content, platform, input_type="text")
                return redirect(url_for("result", result=result))

        elif input_type == "youtube_url":
            youtube_url = request.form.get("youtube_url")
            if youtube_url and platform:
                result = repurpose_text_input(youtube_url, platform, input_type="youtube_url")
                return redirect(url_for("result", result=result))

        elif input_type == "video_file":
            video_file = request.files.get("video_file")
            if video_file and platform:
                file_path = f"temp/{video_file.filename}"
                video_file.save(file_path)
                result = repurpose_text_input(file_path, platform, input_type="video_file")
                os.remove(file_path)
                return redirect(url_for("result", result=result))

    return render_template("index.html")

@app.route("/result")
def result():
    result = request.args.get("result", None)
    return render_template("result.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)