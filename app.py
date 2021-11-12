# Create a sample Flask App
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/about')
def about():
    return '<h1>This is a sample about</h1>'

if __name__ == "__main__":
    app.run(debug=True)