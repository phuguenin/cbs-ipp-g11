import os
from flask import Flask, render_template, request
import giphypop
app = Flask(__name__)

g = giphypop.Giphy()

def get_gifs(keyword):
    if keyword.lower() == "":
        results = ""
    else:
        results = g.search(keyword)
    return results

@app.route("/")
def index():
    return render_template("gifs_index.html")

@app.route("/about")
def about():
    return render_template("gifs_about.html")

@app.route("/results")
def results():
    keyword = request.values.get("keyword")
    results = get_gifs(keyword)
    return render_template("gifs_results.html", keyword=keyword, results=results)


port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)