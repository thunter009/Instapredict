from flask import render_template, request, redirect, url_for, session
from app import app
import os
import pandas as pd
# import likes
# import image_extractor

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route("/", methods=['POST', "GET"])
def index():
    if request.method == 'POST':
        if request.form['submit'] == "Submit":
            handle = request.form['handle']
            call = 'python ./app/scrapers/instaliga/call_scraper.py {:}' \
                .format(handle)
            os.system(call)
            # import ipdb; ipdb.set_trace()
            session['user_data'] = pd.read_json(
                'app/scrapers/instaliga/output.csv')
            return redirect(url_for('results'))

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
        file.save(destination)
    #build redirect logic here
    return render_template("complete.html")


@app.route("/results", methods=['POST'])
def results():

    # import ipdb; ipdb.set_trace()
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    target = os.path.join(APP_ROOT, 'images/image1.jpg')
    image = file.open(target)
    return render_template("results.html")
