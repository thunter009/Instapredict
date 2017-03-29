from flask import render_template, request
from app import app
import os
import pandas as pd


@app.route("/", methods=['POST', "GET"])
def index():
    if request.method == 'POST':
        if request.form['submit'] == "Submit":
            handle = request.form['handle']
            call = 'python ./app/scrapers/instaliga/call_scraper.py {:}' \
                .format(handle)
            os.system(call)
            import ipdb; ipdb.set_trace()
            df = pd.read_csv('app/scrapers/instaliga/output.csv')
    else:
        return render_template('index.html')


@app.route("/upload", methods=['POST'])
def upload():
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    target = os.path.join(APP_ROOT, 'images/')

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        # filename = file.filename
        destination = "/".join([target, "image1.jpg"])
        print(destination)
        file.save(destination)
    return render_template("complete.html")
