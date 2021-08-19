from flask import Flask, send_from_directory, url_for
from flask import render_template

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/resume')
def resume():
    return send_from_directory(directory='static', path='files/Raul_Orban_CV.pdf')

if __name__ == '__main__':
    app.run(debug=True)