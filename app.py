from flask import Flask, render_template, send_from_directory, url_for, redirect, session, flash
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)