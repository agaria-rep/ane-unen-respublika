from flask import Flask, render_template, url_for, request, redirect
import os, requests
from time import sleep

app = Flask(__name__)


@app.route('/')
def index():
    return "index.html"

if __name__ == "__main__":
    app.run()
