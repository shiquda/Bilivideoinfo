import re
import requests
import json
from bs4 import BeautifulSoup

def hot():
    url = 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=all'

    response = requests.get(url)

    data = json.loads(response.text)
    with open("data.txt", "w", encoding='utf-8') as file:
        file.write(str(data))

    video_ids = []
    for video in data['data']['list']:
        id = re.search('BV.*', video['short_link_v2']).group()
        video_ids.append(id)

    with open ("idlist.txt", "w") as file:
        file.write("\n".join(video_ids))