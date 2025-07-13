from bs4 import BeautifulSoup
import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

acc_sid = os.getenv('TWILIO_ACCOUNT_SID')
acc_token = "****************"

client = Client(acc_sid, acc_token)

# Comments line are for live site
# WD7HCYHWCVV87KWZS12LZTBD

web = requests.get("https://appbrewery.github.io/news.ycombinator.com/")

web_pg = BeautifulSoup(web.text, 'html.parser')

name_headls = web_pg.find_all(name='a', class_ = 'storylink')
# i = 0
name_headl_txts = []
name_links = []
for name_headl in name_headls :
    # if not (i % 2):
    #     name_headl_txts.append(name_headl.getText())
    #     name_links.append(name_headl.get('href'))
    name_headl_txts.append(name_headl.getText())
    name_links.append(name_headl.get('href'))
    # i+=1

print(name_headl_txts)
print(name_links)

name_scores = web_pg.find_all(name='span', class_='score')
name_scores_int = [int(score.getText().split()[0]) for score in name_scores]
print(name_scores_int)

highest_score_index = 0
for i in range(len(name_scores_int)):
    if name_scores_int[highest_score_index] < name_scores_int[i] :
        highest_score_index = i

todays_hot_news = name_headl_txts[highest_score_index]
topic_link = name_links[highest_score_index]
highest_score = name_scores_int[highest_score_index]

msg = client.messages.create(body=f"Today's HOT NEWS : {todays_hot_news}\nLink: {topic_link}\n", from_="+19046010428", to="+918910048803")

print(msg.status)

















# with open("41_DAY/website.html") as web_structure :
#     content = web_structure.read()

# soup = BeautifulSoup(content, 'html.parser')

# all_a = soup.find_all("a")
# print(all_a)
# # all_a_str = [each_a.get("href") for each_a in all_a]
# # comp_url = soup.select(selector=".heading")
# # name = soup.find(name='h1', id= 'name')
# # hs = soup.find(name='h3', class_ = 'heading')
# # print(hs)