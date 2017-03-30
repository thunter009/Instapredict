from flask import render_template, request, redirect, url_for, session
from app import app
import os
import pandas as pd
import numpy as np
from app.likes import likes

from app.input_merge_predict import merge_pred as mp
from app.image_extractor import image_extract as ie

import ipdb

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
OUTPUT_PATH = 'app/scrapers/instaliga/output.json'


def call():
    handle = request.form['handle']
    os.system('python ./app/scrapers/instaliga/call_scraper.py {:}'
              .format(handle))


@app.route('/', methods=['POST', "GET"])
def index():
    if request.method == 'POST':
        if request.form['submit'] == "Submit":
            call()
            session['df'] = pd.read_json(OUTPUT_PATH).to_json()
            os.remove(OUTPUT_PATH)
            return redirect(url_for('results'))
        # if request.form['submit'] == "send":
        #     import ipdb; ipdb.set_trace()
        #     session['image'] = ie(crequest.files['image'].read())
        #     return redirect(url_for('index'))
    else:
        return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():

    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    target = os.path.join(APP_ROOT, 'images/')

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        destination = "/".join([target, "image1.jpg"])
        file.save(destination)
    # build redirect logic here
    return render_template("complete.html")


@app.route('/results', methods=['POST', 'GET'])
def results():
    # ipdb.set_trace()

    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    target = os.path.join(APP_ROOT, 'images/image1.jpg')

    user = likes(pd.read_json(session.get('df')))
    image = ie(target)
    results = mp(user, image)

    return render_template("results.html", results=int(np.round(results)))
