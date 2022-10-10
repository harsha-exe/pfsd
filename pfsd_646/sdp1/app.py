from flask import *
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('coverpage.html')


@app.route('/login',)
def login():
    return render_template('index.html')


@app.route('/album')
def contact():
    return render_template('album.html')

@app.route('/customer')
def customer():
    return render_template('custo.html')

if __name__ == "__main__":
    app.run(debug=True)
