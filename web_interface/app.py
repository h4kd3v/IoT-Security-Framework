from flask import Flask, render_template, request, redirect, url_for
from utils.logger import log

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logs')
def view_logs():
    with open('iot_security.log', 'r') as log_file:
        logs = log_file.readlines()
    return render_template('logs.html', logs=logs)

if __name__ == "__main__":
    app.run(debug=True)
