from flask import Flask, render_template, send_from_directory, url_for, redirect, session, flash
from dotenv import load_dotenv
import os
import ngrok

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

if __name__ == '__main__':
    public_url = ngrok.connect(8000)
    print(" * ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}/\"".format(public_url, 8000))

    app.run(debug=True, port=8000)