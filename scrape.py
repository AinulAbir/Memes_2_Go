import requests
from flask import Flask, render_template
import random
app = Flask(__name__)
post_num = 25

# subreddits
star_wars = ['OTmemes', 'prequelmemes', 'sequelmemes']
roses = ['boottoobig']
cats = ['meow_irl']
anime = ['anime_irl', 'Animemes']  # anime_irl 1st post needs to be filtered
dogs = ['woof_irl']
stock = ['youdontsurf']
history = ['historymemes', 'fakehistoryporn', 'trippinthroughtime']
starter_packs = ['starterpacks']
tweets = ['whitepeopletwitter', 'blackpeopletwitter']
infomercials = ['wheredidthesodago']
spongebob = ['bikinibottomtwitter']
christian = ['dankchristianmemes']
relatable = ['Me_irl', 'meirl', 'meirl4meirl']
fellowkids = ['FellowKids']
general = ['meme', 'AdviceAnimals', 'wholesomememes', 'memes', 'dankmemes', 'funny', 'MemeEconomy', 'bonehurtingjuice']

all_subs = (star_wars+roses+cats+anime+dogs+stock+history+starter_packs +
            tweets+infomercials+spongebob+christian+relatable+fellowkids+general)
# ______________________________________________________________________________________________________________________


def scrape(category, sort="hot"):  # sort = rising, new, controversial, top
    ls = []
    limit_value = '10'  # 100 max

    for subs in category:  # uses subreddit(s) from list(s)
        url = f'https://www.reddit.com/r/{subs}/{sort}.json?limit={limit_value}'
        try:
            page_data = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0)'})  # headers to keep reddit :)
        except:
            break
        if "<Response [" in page_data:
            break
        page_data = page_data.json()  # takes the response and resolves it as dict for parsing

        # print(page_data)  # .json to dict validation

        data = page_data['data']  # dict/json object inside the file

        child = data['children']  # data for individual posts
        for i in range(data['dist']): # number of total posts
            p = child[i]['data']  # -> individual posts
            if p["is_self"] is False:  # filters out moderator/owner
                if not any(d['source'] == p['url'] for d in ls):  # duplicate(s) removed via img url

                    if p['title'] is "anime_irl" or "anime❤irl":
                        title = ''
                    else:
                        title = p['title']

                    if p['is_video']:  # for vids
                        media = p['media']
                        v = media['reddit_video']
                        source = v['fallback_url']
                        vid = True
                    else:
                        source = p['url']
                        vid = False

                    link = 'https://reddit.com' + p['permalink']
                    dic = {'title': title, 'link': link, 'source': source, 'is_vid': vid}
                    ls.append(dic)

    return ls


# print(scrape(all_subs))

@app.route("/")
@app.route("/"+'<page>'+'<sort>')
def _all(page=None, sort='hot', category=all_subs, cat="/"):
        data = scrape(category, sort)
        if data:
            return render_template('404.html')
        else:
            total = int(len(data)/post_num)+2
            if page is None:
                data = data[0:post_num]
                random.shuffle(data)
                return render_template('meme.html', data=data, cat=cat, total=total)
            if page is not None:
                page = int(page)
                if page <= total:
                    start = post_num * (int(page) - 1)
                    data = data[start:start + post_num]
                    random.shuffle(data)
                    return render_template('meme.html', data=data, cat=cat, total=total)
                elif page >= total:
                    return render_template('404.html')

@app.route("/anime/")
@app.route("/anime/"+'<page>'+'<sort>')
def _anime(page=None, sort='hot', category=anime, cat="/anime/"):
        data = scrape(category, sort)
        total = int(len(data)/post_num)+2
        if page is None:
            data = data[0:post_num]
            random.shuffle(data)
            return render_template('meme.html', data=data, cat=cat, total=total)
        if page is not None:
            page = int(page)
            if page <= total:
                start = post_num * (int(page) - 1)
                data = data[start:start + post_num]
                random.shuffle(data)
                return render_template('meme.html', data=data, cat=cat, total=total)
            elif page >= total:
                return render_template('404.html')

@app.route("/dogs/")
@app.route("/dogs/"+'<page>'+'<sort>')
def _dogs(page=None, sort='hot', category=dogs, cat="/dogs/"):
        data = scrape(category, sort)
        total = int(len(data)/post_num)+2
        if page is None:
            data = data[0:post_num]
            random.shuffle(data)
            return render_template('meme.html', data=data, cat=cat, total=total)
        if page is not None:
            page = int(page)
            if page <= total:
                start = post_num * (int(page) - 1)
                data = data[start:start + post_num]
                random.shuffle(data)
                return render_template('meme.html', data=data, cat=cat, total=total)
            elif page >= total:
                return render_template('404.html')

@app.route("/general/")
@app.route("/general/"+'<page>'+'<sort>')
def _general(page=None, sort='hot', category=general, cat="/general/"):
        data = scrape(category, sort)
        total = int(len(data)/post_num)+2
        if page is None:
            data = data[0:post_num]
            random.shuffle(data)
            return render_template('meme.html', data=data, cat=cat, total=total)
        if page is not None:
            page = int(page)
            if page <= total:
                start = post_num * (int(page) - 1)
                data = data[start:start + post_num]
                random.shuffle(data)
                return render_template('meme.html', data=data, cat=cat, total=total)
            elif page >= total:
                return render_template('404.html')

@app.route("/spongebob/")
@app.route("/spongebob/"+'<page>'+'<sort>')
def _spongbob(page=None, sort='hot', category=spongebob, cat="/spongebob/"):
        data = scrape(category, sort)
        total = int(len(data)/post_num)+2
        if page is None:
            data = data[0:post_num]
            random.shuffle(data)
            return render_template('meme.html', data=data, cat=cat, total=total)
        if page is not None:
            page = int(page)
            if page <= total:
                start = post_num * (int(page) - 1)
                data = data[start:start + post_num]
                random.shuffle(data)
                return render_template('meme.html', data=data, cat=cat, total=total)
            elif page >= total:
                return render_template('404.html')

@app.route("/star-wars/")
@app.route("/star-wars/"+'<page>'+'<sort>')
def _star_wars(page=None, sort='hot', category=star_wars, cat="/star-wars/"):
        data = scrape(category, sort)
        total = int(len(data)/post_num)+2
        if page is None:
            data = data[0:post_num]
            random.shuffle(data)
            return render_template('meme.html', data=data, cat=cat, total=total)
        if page is not None:
            page = int(page)
            if page <= total:
                start = post_num * (int(page) - 1)
                data = data[start:start + post_num]
                random.shuffle(data)
                return render_template('meme.html', data=data, cat=cat, total=total)
            elif page >= total:
                return render_template('404.html')

@app.route("/cats/")
@app.route("/cats/"+'<page>'+'<sort>')
def _cats(page=None, sort='hot', category=cats, cat="/cats/"):
        data = scrape(category, sort)
        total = int(len(data)/post_num)+2
        if page is None:
            data = data[0:post_num]
            random.shuffle(data)
            return render_template('meme.html', data=data, cat=cat, total=total)
        if page is not None:
            page = int(page)
            if page <= total:
                start = post_num * (int(page) - 1)
                data = data[start:start + post_num]
                random.shuffle(data)
                return render_template('meme.html', data=data, cat=cat, total=total)
            elif page >= total:
                return render_template('404.html')

@app.route("/history/")
@app.route("/history/"+'<page>'+'<sort>')
def _history(page=None, sort='hot', category=history, cat="/history/"):
        data = scrape(category, sort)
        total = int(len(data)/post_num)+2
        if page is None:
            data = data[0:post_num]
            random.shuffle(data)
            return render_template('meme.html', data=data, cat=cat, total=total)
        if page is not None:
            page = int(page)
            if page <= total:
                start = post_num * (int(page) - 1)
                data = data[start:start + post_num]
                random.shuffle(data)
                return render_template('meme.html', data=data, cat=cat, total=total)
            elif page >= total:
                return render_template('404.html')

@app.route("/roses/")
@app.route("/roses/"+'<page>'+'<sort>')
def _roses(page=None, sort='hot', category=roses, cat="/roses/"):
        data = scrape(category, sort)
        total = int(len(data)/post_num)+2
        if page is None:
            data = data[0:post_num]
            random.shuffle(data)
            return render_template('meme.html', data=data, cat=cat, total=total)
        if page is not None:
            page = int(page)
            if page <= total:
                start = post_num * (int(page) - 1)
                data = data[start:start + post_num]
                random.shuffle(data)
                return render_template('meme.html', data=data, cat=cat, total=total)
            elif page >= total:
                return render_template('404.html')

@app.route("/infomercials/")
@app.route("/infomercials/"+'<page>'+'<sort>')
def _infomercials(page=None, sort='hot', category=infomercials, cat="/infomercials/"):
        data = scrape(category, sort)
        total = int(len(data)/post_num)+2
        if page is None:
            data = data[0:post_num]
            random.shuffle(data)
            return render_template('meme.html', data=data, cat=cat, total=total)
        if page is not None:
            page = int(page)
            if page <= total:
                start = post_num * (int(page) - 1)
                data = data[start:start + post_num]
                random.shuffle(data)
                return render_template('meme.html', data=data, cat=cat, total=total)
            elif page >= total:
                return render_template('404.html')

@app.route("/stock/")
@app.route("/stock/"+'<page>'+'<sort>')
def _stock(page=None, sort='hot', category=stock, cat="/stock/"):
        data = scrape(category, sort)
        total = int(len(data)/post_num)+2
        if page is None:
            data = data[0:post_num]
            random.shuffle(data)
            return render_template('meme.html', data=data, cat=cat, total=total)
        if page is not None:
            page = int(page)
            if page <= total:
                start = post_num * (int(page) - 1)
                data = data[start:start + post_num]
                random.shuffle(data)
                return render_template('meme.html', data=data, cat=cat, total=total)
            elif page >= total:
                return render_template('404.html')

@app.route("/tweets/")
@app.route("/tweets/"+'<page>'+'<sort>')
def _tweets(page=None, sort='hot', category=tweets, cat="/tweets/"):
        data = scrape(category, sort)
        total = int(len(data)/post_num)+2
        if page is None:
            data = data[0:post_num]
            random.shuffle(data)
            return render_template('meme.html', data=data, cat=cat, total=total)
        if page is not None:
            page = int(page)
            if page <= total:
                start = post_num * (int(page) - 1)
                data = data[start:start + post_num]
                random.shuffle(data)
                return render_template('meme.html', data=data, cat=cat, total=total)
            elif page >= total:
                return render_template('404.html')

@app.route("/starter-packs/")
@app.route("/starter-packs/"+'<page>'+'<sort>')
def _starter_packs(page=None, sort='hot', category=starter_packs, cat="/starter-packs/"):
        data = scrape(category, sort)
        total = int(len(data)/post_num)+2
        if page is None:
            data = data[0:post_num]
            random.shuffle(data)
            return render_template('meme.html', data=data, cat=cat, total=total)
        if page is not None:
            page = int(page)
            if page <= total:
                start = post_num * (int(page) - 1)
                data = data[start:start + post_num]
                random.shuffle(data)
                return render_template('meme.html', data=data, cat=cat, total=total)
            elif page >= total:
                return render_template('404.html')

@app.route("/christian/")
@app.route("/christian/"+'<page>'+'<sort>')
def _christian(page=None, sort='hot', category=christian, cat="/christian/"):
        data = scrape(category, sort)
        total = int(len(data)/post_num)+2
        if page is None:
            data = data[0:post_num]
            random.shuffle(data)
            return render_template('meme.html', data=data, cat=cat, total=total)
        if page is not None:
            page = int(page)
            if page <= total:
                start = post_num * (int(page) - 1)
                data = data[start:start + post_num]
                random.shuffle(data)
                return render_template('meme.html', data=data, cat=cat, total=total)
            elif page >= total:
                return render_template('404.html')

@app.route("/relateable/")
@app.route("/relateable/"+'<page>'+'<sort>')
def _relateable(page=None, sort='hot', category=christian, cat="/relateable/"):
        data = scrape(category, sort)
        total = int(len(data)/post_num)+2
        if page is None:
            data = data[0:post_num]
            random.shuffle(data)
            return render_template('meme.html', data=data, cat=cat, total=total)
        if page is not None:
            page = int(page)
            if page <= total:
                start = post_num * (int(page) - 1)
                data = data[start:start + post_num]
                random.shuffle(data)
                return render_template('meme.html', data=data, cat=cat, total=total)
            elif page >= total:
                return render_template('404.html')

@app.route("/fellow-kids/")
@app.route("/fellow-kids/"+'<page>'+'<sort>')
def _fellow_kids(page=None, sort='hot', category=christian, cat="/fellow-kids/"):
        data = scrape(category, sort)
        total = int(len(data)/post_num)+2
        if page is None:
            data = data[0:post_num]
            random.shuffle(data)
            return render_template('meme.html', data=data, cat=cat, total=total)
        if page is not None:
            page = int(page)
            if page <= total:
                start = post_num * (int(page) - 1)
                data = data[start:start + post_num]
                random.shuffle(data)
                return render_template('meme.html', data=data, cat=cat, total=total)
            elif page >= total:
                return render_template('404.html')

app.run(debug=True)




