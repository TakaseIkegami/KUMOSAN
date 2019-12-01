import random
from bs4 import BeautifulSoup
import urllib.request

# Meigen
def meigen():
    response_string = ''
    d1960 = random.randint(1,1960)
    print(d1960)
    if d1960 == 1:
        response_string = "あぁ＾〜ワイス〜〜〜 :snowflake: - クロレラ"
    else:
        meigen_url = "http://www.meigensyu.com/quotations/index/random"
        meigen_html = urllib.request.urlopen(meigen_url)
        soup = BeautifulSoup(meigen_html, "html.parser")

        meigen = soup.select_one("#contents_box > div:nth-of-type(8) > div.text")
        author = soup.select_one("#contents_box > div:nth-of-type(8) > div.link > ul > li:nth-child(1) > a")
        for mg in meigen:
            text1 = mg
        for at in author:
            text2 = at
        response_string = mg + " ― " + at
    return response_string
