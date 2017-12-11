#!flask-sample/app.py

from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, host='0.0.0.0')
    #app.run(debug=True, host='0.0.0.0')
    #app.run()
