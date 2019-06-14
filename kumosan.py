# -*- coding:utf-8 -*-
import discord
import wikipedia
import requests
import json
import random
import subprocess
import time
import urllib.request
import datetime
import os
from bs4 import BeautifulSoup

client = discord.Client()
################# Don't touch. ################
kumo_san = '╭◜◝ ͡ ◜◝╮ \n(   •ω•　  ) \n╰◟◞ ͜ ◟◞╯ < '
################# Don't touch. ################

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
 
    ######## 裏モード ########
    main_chat='任意のチャンネルID'
    bot_salon='任意のチャンネルID'
    if message.channel == client.get_channel('main_chat') and message.author.id == 'bot_salon':
        try:
            text = message.content
            selector = bot_salon
            index_st = text.find(' ')+1
            index_ed = text.find(' ')
            search_channel = text[:index_ed]
            search_text = text[index_st:]
            print(search_channel)
            print(search_text)
            if search_channel == 'bot':
                selector = bot_salon
            elif search_channel == 'main':
                selector = main_chat
            else:
                selector = bot_salon
            print(selector)
            msg = kumo_san + search_text
            await client.send_message(client.get_channel(selector), msg)
            return msg
        except Exception as e:
            print(e)
            raise e 
    #########################

    # 「雲さん」で始まるか調べる
    elif message.content.startswith("雲さん"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            try:
                user_name = message.author.name
                user_id = message.author.id
                text = message.content
                print(text)

                msg =  kumo_san + user_name + 'さん '
                #msg = user_name + 'さん '
                if text == ('雲さん'):
                    msg = 'はい！ご用でしょうか！'
                elif text.find('おは') > -1:
                    msg += 'おはようございます！'
                elif text.find('こんにちは') > -1 or text.find('こんにちわ') > -1 or text.find('こんちゃ') > -1 or text.find('やあ') > -1 or text.find('おっす') > -1 or text.find('こんにち') > -1:
                    msg += 'こんにちは！'
                elif text.find('こんばんは') > -1 or text.find('こんばんわ') > -1 or text.find('ばんわ') > -1 or text.find('こんばん') > -1:
                    msg += 'こんばんは！'
                elif text.find('おつ') > -1 or text.find('疲') > -1 or text.find('お先') > -1 or text.find('おち') > -1 or text.find('落ち') > -1:
                    msg += 'おつかれさまです＾〜'
                elif text.find('おやす') > -1:
                    msg += 'おやすみなさーい'
                elif text.find('ありがと') > -1 or text.find('thank') > -1 or text.find('thx') > -1:
                    msg += 'お役に立てたならなによりです！'
                elif text.find('おみくじ') > -1:
                    msg += omikuji()
                elif text.find('大丈夫') > -1 or text.find('生きてる') > -1 or text.find('元気') > -1 or text.find('死んでない') > -1:
                    msg = '大丈夫です！'
                elif text.find('好き') > -1 or text.find('愛') > -1 or text.find('すき') > -1:
                    msg = 'えへへ'
                elif text.find('自己紹介して') > -1:
                    msg = 'はい！はじめまして。Takaseさんに作られたヒヨッ子botの雲と申します。趣味は素数を数えることです。皆さんのお役に立てすようにがんばりますので、どうぞよろしくお願いします！:cloud:'
                elif text.find('help') > -1 or text.find('-h') > -1:
                    msg += '<あらかじめディスコ内に投稿しておいた使い方コメントのリンクを貼ってね>'
                elif text.find('慰めて') > -1 or text.find('なぐさめて') > -1 or text.find('アドバイス') > -1 or text.find('助言') > -1:
                    msg = meigen()
                elif text.find('なろう') > -1:
                    msg = narouSearch(text)
                elif text.find('犯罪係数') > -1 or text.find('ドミネータ') > -1 or text.find('サイコパス') > -1 or text.find('色相') > -1 or text.find('シビュラ') > -1:
                    msg = kumo_san + dominator(text)
                elif text.find('minecraft') > -1:
                    msg += sendSignalTominecraft(text)
                elif text.find('wp') > -1:
                    msg = kumo_san + waruiko_point(text, user_id)
                elif text.find('マインスイーパ') > -1 or text.find('まいんすいーぱ') > -1:
                    msg += '出題！\n' + minesweeper(text)
                elif text.find('級') > -1 or text.find('遊ぼ') > -1 or text.find('遊んで') > -1 or text.find('あそぼ') > -1 or text.find('あそんで') > -1:
                    msg += 'マインスイーパーしましょう！\n' + minesweeper(text)
                elif text.find('座') > -1:
                    msg += uranai(text)
                elif text.find('って何') > -1:
                    msg += wikipediaSearch(text)
                elif text.find('天気') > -1:
                    msg += getWeatherInformation(text)
                elif text.find('は素数') > -1:
                    msg += primarity_test(text, 50)
                else:
                    msg += 'その言葉は知らなかったから調べたよ。\n' + wikipediaSearch(text)
                # メッセージが送られてきたチャンネルへメッセージを送ります
                await client.send_message(message.channel, msg)
                return msg
            except Exception as e:
                print(e)
                raise e

# Get Weather Infomation
def getWeatherInformation(text):
    weather_api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
    response_string = ''
    city_id = ''
    if text.find('長野') > -1:
        city_id = '200010'
    elif text.find('大阪') > -1:
        city_id = '270000'
    elif text.find('東京') > -1:
        city_id = '130010'
    elif text.find('北海道') > -1 or text.find('札幌') > -1:
        city_id = '016010'
    elif text.find('愛知') > -1 or text.find('名古屋') > -1:
        city_id = '230010'
    elif text.find('静岡') > -1:
        city_id = '220010'
    elif text.find('佐賀') > -1:
        city_id = '410010'
    else:
        city_id = '130010'
        response_string += '場所が聞き取れなかったので取り敢えず'

    try:
        params = {'city':city_id}
        response = requests.get(weather_api_url,params=params)
        #print(params)
        #print(response)
        response_dict = json.loads(response.text)
        title = response_dict["title"]
        description = response_dict["description"]["text"]
        response_string += title + "です！\n\n"
        forecasts_array = response_dict["forecasts"]
        forcast_array = []
        for forcast in forecasts_array:
            telop = forcast["telop"]
            telop_icon = ''
            if telop.find('雪') > -1:
                telop_icon = ':showman:'
            elif telop.find('雷') > -1:
                telop_icon = ':thunder_cloud_and_rain:'
            elif telop.find('晴') > -1:
                if telop.find('曇') > -1:
                    telop_icon = ':partly_sunny:'
                elif telop.find('雨') > -1:
                    telop_icon = ':partly_sunny_rain:'
                else:
                    telop_icon = ':sunny:'
            elif telop.find('雨') > -1:
                telop_icon = ':umbrella:'
            elif telop.find('曇') > -1:
                telop_icon = ':cloud:'
            else:
                telop_icon = ':fire:'

            temperature = forcast["temperature"]
            min_temp = temperature["min"]
            max_temp = temperature["max"]
            temp_text = ''
            if min_temp is not None:
                if len(min_temp) > 0:
                    temp_text += '\n最低気温は' + min_temp["celsius"] + "℃"
            if max_temp is not None:
                if len(max_temp) > 0:
                    temp_text += '\n最高気温は' + max_temp["celsius"] + "℃"

            forcast_array.append(forcast["dateLabel"] + ' ' + telop + telop_icon + temp_text)
        if len(forcast_array) > 0:
            response_string += '\n\n'.join(forcast_array)
        response_string += '\n\n' + description
    except Exception as e:
        response_string = '天気検索でエラーです＞＜ :cold_sweat:\n' + e.message + '\n' + str(e)
    return response_string

# Search from Wikipedia
def wikipediaSearch(text):
    response_string = ''
    wikipedia.set_lang('ja')
    index_st = text.find(' ')
    index_ed = text.find('って何')
    search_text = text[index_st:index_ed]
    search_response = wikipedia.search(search_text)
    print(search_response)
    if len(search_response) > 0:
        try:
            wiki_page = wikipedia.page(search_response[0])
        except Exception as e:
            try:
                wiki_page = wikipedia.page(search_response[1])
            except Exception as e:
                response_string = 'お探しの言葉ではエラーを起こしました！:cold_sweat:\n' + e.message + '\n' + str(e)
        response_string = '説明しよう！\n'
        response_string += wiki_page.content[0:200] + '.....\n'
        response_string += wiki_page.url
    else:
        response_string = '今はまだ見つけられないンゴ…でも頑張って見つけられるようになるゾ〜！'

    return response_string

# Miller-Rabin Primality Test
def primarity_test(text, k):
    response_string = ''
    index_st = text.find(' ')
    index_ed = text.find('は素数')
    q = int(text[index_st:index_ed])
    if q == 2:
        response_string = str(q) + 'は素数です！:laughing:'
        return response_string
    if q < 2 or q & 1 == 0:
        response_string = str(q) + 'は素数じゃないです！:rage:'
        return response_string

    d = (q - 1) >> 1
    while d & 1 == 0:
        d >>= 1

    for i in range(k):
        a = random.randint(1, q-1)
        t = d
        y = pow(a, t, q)
        while t != q-1 and y != 1 and y != q-1:
            y = pow(y, 2, q)
            t <<= 1
        if y != q-1 and t & 1 == 0:
            response_string = str(q) + 'は素数じゃないです！:rage:'
            return response_string
        response_string = str(q) + 'は素数です！:wink:'
    return response_string

# Omikuji
def omikuji():
    response_string = ''
    lots = ["大吉", "吉", "中吉", "小吉", "半吉", "末吉", "末小吉", "平", "凶", "小凶", "半凶", "末凶", "大凶", "未分"]
    random.shuffle(lots)
    lot = lots[0]
    print(lot)
    response_string = "あなたの運勢は...ｶﾞｼｬｶﾞｼｬｶﾞｼｬｶﾞｼｬ...\n\n　　　　" + lot + "　ですね！"

    return response_string

# send some signals to minecraft
def sendSignalTominecraft(text):
    response_string = ''
    if text.find("minecraft kick") > -1:
        index_st = text.find('kick ') + 5
        #index_ed = text.find('')
        user_name = text[index_st:]
        response_string = "了解いたしました。"+ user_name + "さんをキックします。"
        try:
            subprocess.call(["sh", "minecraft_scripts/kick.sh", user_name])
        except Exception as e:
            response_string = '構文エラーです＞＜ :cold_sweat:\n' + e.message + '\n' + str(e)
        '''
    elif text == "雲さん minecraft restart":
        response_string = "了解いたしました。マイクラを再起動します。"
        #スクリーン及び起動スクリプトへのkillコマンド挿入
        try:
            subprocess.call(["sh", "minecraft_scripts/quit.sh"])
        except Exception as e:
            response_string = '構文エラーです＞＜ :cold_sweat:\n' + e.message + '\n' + str(e)
        #スクリーン及び起動スクリプトの実行コマンド挿入
        try:
            subprocess.call(["sh", "minecraft_scripts/restart.sh"])
        except Exception as e:
            response_string = '構文エラーです＞＜ :cold_sweat:\n' + e.message + '\n' + str(e)
        '''
    else:
        response_string = "構文エラーです＞＜ :cold_sweat:\n 正しく入力してね！"

    return response_string

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

# Meigen
def meigen():
    response_string = ''
    d1960 = random.randint(1,1960)
    print(d1960)
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

# Narou
def narouSearch(text):
    response_string = ''
    narou_api_url = 'https://api.syosetu.com/novelapi/api'#?out=json&order=hyoka'
    params = {'out':'json'}
    if text.find('評価') > -1:
        if text.find('高') > -1:
            params.update({'order':'hyoka'})
        elif text.find('低') > -1:
            params.update({'order':'hyokaasc'})
        else:
            params.update({'order':'new'})
    response = requests.get(narou_api_url,params=params).text
    #response.encoding = response.apparent_encoding
    #response.encoding = "Shift_JIS"
    response_dict = json.loads(response)
    if text.find('-d') > -1:
        for rd in response_dict:
            try:
                title = json.dumps(rd['title'], ensure_ascii=False)
                #print(title)
                writer = json.dumps(rd['writer'], ensure_ascii=False)
                story = json.dumps(rd['story'], ensure_ascii=False)
                response_string += "\nタイトル: " + title + "\n作　　者: " + writer + "\nあらすじ: " + story + "\n\n"
            except Exception as e:
                pass
    else:
        for rd in response_dict:
            try:
                title = json.dumps(rd['title'], ensure_ascii=False)
                response_string += title + "\n"
            except Exception as e:
                pass
    response_string = '{:.2000}'.format(response_string)
    return response_string

def dominator(text):
    response_string = ''
    date = datetime.datetime.today().strftime("%Y/%m/%d")
    index_st = text.find('<')+1
    index_ed = text.find('>')-1
    search_text = text[index_st:index_ed]
    print(search_text)
    random.seed(date+search_text)
    crime_factor = random.randint(0, 1000)
    if crime_factor<100:
        response_string = "犯罪係数 **"+ str(crime_factor) + "** 。\n犯罪係数アンダー100。執行対象ではありません。トリガーをロックします。"
    elif 100<=crime_factor and crime_factor<300:
        response_string = "犯罪係数 **"+ str(crime_factor) + "** 。\n犯罪係数オーバー100。執行モード ノンリーサル パラライザー。\n慎重に照準を定め 対象を制圧して下さい。"
    elif 300<=crime_factor and crime_factor<900:
        response_string = "犯罪係数 **"+ str(crime_factor) + "** 。\n犯罪係数オーバー300。執行モード リーサル エリミネーター。\n慎重に照準を定め 対象を排除して下さい。"
    elif 900<=crime_factor:
        response_string = "犯罪係数 **"+ str(crime_factor) + "** 。\n執行モード デストロイ デコンポーザー。\n対象を完全排除します。ご注意下さい。 "
    return response_string

def waruiko_point(text, user_id):
    response_string = ''
    index_st = text.find('wp ')+3
    index_ed = text.find(' <')
    index_st2 = text.find('<@')+2
    index_ed2 = text.find('>')
    target = text[index_st2:index_ed2]
    path = 'users/'+target+".txt"
    if os.path.isfile(path) == False:
        with open(path, mode='w') as f:
            f.write(str(0))
    if text.find('-s') > -1 or text.find('--show') > -1:
        with open(path) as f:
            s = f.read()
            s = int(s)
            response_string = "現在の悪い子ポイントは **"+ str(s) +"** ポイントです。"
            return response_string
    if target == user_id:
        response_string = "自分の悪い子ポイントは操作できないよ！"
        return response_string
    #print("target", target)
    #print("path", path)
    #print(text[index_st:index_st+1])
    #print(text[index_st+1:index_ed])
    if 10<int(text[index_st+1:index_ed]):
        response_string = "悪い子ポイントの付与は一度に10ポイントまでです！"
        return response_string
    else:
        if text[index_st:index_st+1] == '+':
            wp = int(text[index_st+1:index_ed])
        elif text[index_st:index_st+1] == '-':
            wp = -1 * int(text[index_st+1:index_ed])
        else:
            print("ERROR")
    with open(path) as f:
        s = f.read()
        s = int(s) + wp
    with open(path, mode='w') as f:
        f.write(str(s))
    response_string = '悪い子ポイントを **' + str(wp) + '** しました。\nこれで悪い子ポイントは **'+str(s)+'** ポイントです。'
    return response_string

def minesweeper(text):
    response_string = ''
    if text.find('低級') > -1:
        difficulty = 0.1
        rows = 8
        clear_range = [3, 4]
        response_string += '[低級]'
    elif text.find('中級') > -1:
        difficulty = 0.15
        rows = 10
        clear_range = [3, 5]
        response_string += '[中級]'
    elif text.find('上級') > -1:
        difficulty = 0.2
        rows = 12
        clear_range = [4, 7]
        response_string += '[上級]'
    elif text.find('超級') > -1:
        difficulty = 0.25
        rows = 12
        clear_range = [4, 6]
        response_string += '[超級]'
    elif text.find('雲さん級') > -1:
        difficulty = 0.3
        rows = 12
        clear_range = [4, 6]
        response_string += '[雲さん級]'
    else:
        difficulty = 0.15
        rows = 10
        clear_range = [3, 5]
        response_string += '[中級]'
    response_string += '\n'
    # 盤面の初期化、および爆弾の設置(100)
    stage = [[100 if random.random()<difficulty else 0 for x in range(rows+1)] for y in range(rows+1)]

    # 爆弾を探索し、周辺マスをカウントアップ
    for x in range(rows):
        for y in range(rows):
            try:
                if stage[x][y] >= 100:
                    stage[x-1][y-1] += 1
                    stage[x][y-1]+=1
                    stage[x+1][y-1] += 1

                    stage[x-1][y] += 1
                    #stage[x][y] += 1
                    stage[x+1][y] += 1
                    
                    stage[x-1][y+1] += 1
                    stage[x][y+1] += 1
                    stage[x+1][y+1] += 1
            except (IndexError) as e:
                pass

    # 伏せ字への変換
    for x in range(rows):
        for y in range(rows):
            if clear_range[0]<=x<=clear_range[1] and clear_range[0]<=y<=clear_range[1]:
                if stage[x][y] == 0:
                    stage[x][y] = ":zero:"
                elif stage[x][y] == 1:
                    stage[x][y] = ":one:"
                elif stage[x][y] == 2:
                    stage[x][y] = ":two:"
                elif stage[x][y] == 3:
                    stage[x][y] = ":three:"
                elif stage[x][y] == 4:
                    stage[x][y] = ":four:"
                elif stage[x][y] == 5:
                    stage[x][y] = ":five:"
                elif stage[x][y] == 6:
                    stage[x][y] = ":six:"
                elif stage[x][y] == 7:
                    stage[x][y] = ":seven:"
                elif stage[x][y] == 8:
                    stage[x][y] = ":eight:"
                elif stage[x][y] >= 100:
                    stage[x][y] = "||:bomb:||"
            else:
                if stage[x][y] >= 100:
                    stage[x][y] = "||:bomb:||"
                elif stage[x][y] == 0:
                    stage[x][y] = "||:zero:||"
                elif stage[x][y] == 1:
                    stage[x][y] = "||:one:||"
                elif stage[x][y] == 2:
                    stage[x][y] = "||:two:||"
                elif stage[x][y] == 3:
                    stage[x][y] = "||:three:||"
                elif stage[x][y] == 4:
                    stage[x][y] = "||:four:||"
                elif stage[x][y] == 5:
                    stage[x][y] = "||:five:||"
                elif stage[x][y] == 6:
                    stage[x][y] = "||:six:||"
                elif stage[x][y] == 7:
                    stage[x][y] = "||:seven:||"
                elif stage[x][y] == 8:
                    stage[x][y] = "||:eight:||"
                elif 9 <= stage[x][y] < 100:
                    return minesweeper(text)
            response_string += str(stage[x][y])
        response_string += "\n"
    return response_string

client.run("ここにトークンを書いてね")
