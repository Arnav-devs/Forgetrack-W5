from flask import Flask, render_template, request, redirect, jsonify
import json
import random
import string
from pathlib import Path

app = Flask(__name__)

FILE_PATH = Path("data.json")

def initialize():
    if not FILE_PATH.exists():
        with FILE_PATH.open("w") as file:
            json.dump({}, file)

def get_links():
    with FILE_PATH.open("r") as file:
        return json.load(file)

def store_links(links):
    with FILE_PATH.open("w") as file:
        json.dump(links, file, indent=4)

def create_short_code(length=6):
    characters = string.ascii_letters + string.digits

    while True:
        new_code = "".join(random.choices(characters, k=length))

        if new_code not in get_links():
            return new_code

initialize()

@app.route("/")
def index():
    return render_template(
        "index.html",
        error=None,
        short_url=None
    )

@app.route("/shorten", methods=["POST"])
def shorten_link():
    original_url = request.form.get("url", "").strip()

    if not original_url.startswith(("http://", "https://")):
        return render_template(
            "index.html",
            error="Please enter a valid URL starting with http:// or https://",
            short_url=None
        )

    links = get_links()
    code = create_short_code()

    links[code] = {
        "url": original_url,
        "clicks": 0
    }
    store_links(links)
    return render_template(
        "index.html",
        short_url=f"{request.host_url}s/{code}",
        error=None
    )

@app.route("/s/<code>")
def open_link(code):

    links = get_links()
    link = links.get(code)

    if link is None:
        return render_template("error.html"), 404
    link["clicks"] += 1

    store_links(links)
    return redirect(link["url"])

@app.route("/dashboard")
def show_dashboard():
    return render_template(
        "dashboard.html",
        links=get_links()
    )

@app.route("/api/links")
def get_api_data():
    return jsonify(get_links())

if __name__ == "__main__":
    app.run(debug=True)