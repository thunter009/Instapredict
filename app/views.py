from flask import render_template, request
from app import app
import os

# @app.route('/index')
# def index():
#     if request.form['submit'] == "Submit":
#         print ("=" * 50)


#     return render_template('index.html',
#                            title='Instapredict'
#                            )

@app.route("/", methods=['POST', "GET"])
def index():
    if request.method == 'POST':
        print ("*" * 50)
        if request.form['submit'] == "Submit":
            print ("=" * 50)

            os.system('python ./app/scrapers/instaliga/call_scraper.py')
            print ("=" * 50)
            print('Done')
    else:
        return render_template('index.html')
