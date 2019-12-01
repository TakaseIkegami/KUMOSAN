import requests
import datetime

# Uranai
def uranai(text):
    response_string = ''
    seiza = 100
    date = datetime.datetime.today().strftime("%Y/%m/%d")
    index_st = text.find(' ')+1
    index_ed = text.find('座')+1
    search_text = text[index_st:index_ed]
    print(search_text)
    seiza_list = ("牡羊座", "牡牛座", "双子座", "蟹座", "獅子座", "乙女座", "天秤座", "蠍座", "射手座", "山羊座", "水瓶座", "魚座")
    seiza_list2 = ("おひつじ座", "おうし座", "ふたご座", "かに座", "しし座", "おとめ座", "てんびん座", "さそり座", "いて座", "やぎ座", "みずがめ座", "うお座")
    try:
        seiza = seiza_list.index(search_text)
    except:
        try:
            seiza = seiza_list2.index(search_text)
        except Exception as e:
            response_string = "君の星が…見えない… :cloud:"
    try:
        res = requests.get(url='http://api.jugemkey.jp/api/horoscope/free/'+ date)
        txt = res.json()["horoscope"][date][seiza]
        job = emoji(int(txt["job"]), "job")
        money = emoji(int(txt["money"]), "money")
        love = emoji(int(txt["love"]), "love")
        total = emoji(int(txt["total"]), "total")
        response_string = "今日の**" + txt["sign"] + "**の運勢は。。。**" + str(txt["rank"]) + "位**！\n" + txt["content"] + "\nラッキーアイテムは**" + txt["item"] + "**で、ラッキーカラーは**" + txt["color"] + "**。\n仕事運："+job+"\n金　運：" + money + "\n恋愛運：" + love + "\nトータルは..." + total + "です！良い一日を！"
        #print(response_string)
    except Exception as e:
        print("君の星が…見えない… :cloud:")
    return response_string

def emoji(number, category):
    res = ''
    for i in range(number):
        if category == 'job':
            res += ':briefcase: '
        elif category == 'money':
            res += ':moneybag: '
        elif category == 'love':
            res += ':heart: '
        elif category == 'total':
            res += ':star: '
    return res
