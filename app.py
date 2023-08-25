from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        return "<h1>Hello</h1>"

    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(_):
    return redirect("/")

if __name__ == "__main__": app.run(debug = True)