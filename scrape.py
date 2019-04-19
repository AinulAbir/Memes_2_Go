import requests


# # testing with the offline copy
# import json
# url = open("data.json", 'r', encoding='utf-8')
# data = json.load(url)
# url.close()

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


def Scrape(category):
    ls = []
    limit_value = '10'  # 100 max

    for subs in category:  # uses subreddit(s) from list(s)
        url = 'https://www.reddit.com/r/'+subs+'.json?limit='+limit_value
        page = requests.get(url, headers={'User-agent': 'chrome'})  # headers to keep reddit :)
        page_data = page.json()  # takes the response and resolves it as dict for parsing

        # print(type(page_data))  # .json to dict validation

        data = page_data['data']  # dict/json object inside the file

        child = data['children']  # data for individual posts
        for i in range(data['dist']): # number of total posts
            p = child[i]['data']  # -> individual posts
            if p["is_self"] is False:  # filters out moderator/owner
                if not any(d['source'] == p['url'] for d in ls):  # duplicate(s) removed via img url

                    # if p['title'] is "anime_irl" or "anime❤irl":
                    #     title = ''      # fix this shit
                    # else:
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



