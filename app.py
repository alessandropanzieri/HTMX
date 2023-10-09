from flask import (
    Flask,
    redirect,
    render_template
)

app = Flask(__name__)

@app.get("/")
def get():
    return render_template("index.html")

@app.post("/")
def post():
    return "<h1>Hello</h1>"

@app.errorhandler(404)
def page_not_found(_):
    return redirect("/")

if __name__ == "__main__": app.run()
