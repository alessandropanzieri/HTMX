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

if __name__ == "__main__": app.run()
