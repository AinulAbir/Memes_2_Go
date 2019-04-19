import scrape
from scrape import general, Scrape, stock
from flask import Flask, render_template
import random
app = Flask(__name__)
post_num = 25


@app.route("/")
def homepage():
    return '<meta http-equiv="refresh" content="0; url=/general/"/>'

def webapp(cat_name, cat):
    # cato = "/general/"
    random.shuffle(cat)
    data = Scrape(cat)
    @app.route(cat_name)
    @app.route(cat_name+'<page>')
    def _f(page=None, cat=cat, data = data):
        total = int(len(data)/post_num)+2
        if page is None:
            return render_template('meme.html', data=data[0:post_num], cat=str(cat_name), total=total)
        if page is not None:
            page = int(page)
            if page <= total:
                start = post_num * (int(page) - 1)
                return render_template('meme.html', data=data[start:start + post_num], cat=str(cat_name), total=total)
            elif page >= total:
                return render_template('404.html')


webapp("/general/", general)

app.run(debug=True)
