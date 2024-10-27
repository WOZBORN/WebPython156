from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/stories")
def hello():
    return render_template("stories.html")

if __name__ == "__main__":
    app.run()