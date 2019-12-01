# -*- coding:utf-8 -*-
import discord
#import wikipedia
#import requests
#import json
#import random
#import re
#import subprocess
#import time
#import urllib.request
#import datetime
#import os
#from bs4 import BeautifulSoup
from lib import wiki
from lib import weather
from lib import waruiko_point
from lib import uranai
from lib import primarity_test
from lib import omikuji
from lib import narou
from lib import modokicraft
from lib import minesweeper
from lib import meigen
from lib import keisuke_honda
from lib import dominator
from lib import dice

from resources import token
from resources import channels
#import playMusic

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
    channel = message.channel

    ######## 裏モード ########
    if message.channel == client.get_channel(XXXXXXXXXXXXXXXXXX) and message.author.id == XXXXXXXXXXXXXXXXXX:
        try:
            text = message.content
            main_chat=XXXXXXXXXXXXXXXXXX
            bot_salon=XXXXXXXXXXXXXXXXXX
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
            await client.get_channel(selector).send(msg)
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
                elif text.find('起きて') > -1:
                    msg = 'zzZ...ﾊｯ!Σ(･ω･;)\n'+ kumo_san + 'おはようございます！\nおおおオキテマシタヨ！！！'
                elif text.find('ありがと') > -1 or text.find('thank') > -1 or text.find('thx') > -1:
                    msg += 'お役に立てたならなによりです！'
                elif text.find('おみくじ') > -1:
                    msg += omikuji.omikuji()
                elif text.find('大丈夫') > -1 or text.find('生きてる') > -1 or text.find('元気') > -1 or text.find('死んでない') > -1:
                    msg = '大丈夫です！'
                elif text.find('好き') > -1 or text.find('愛') > -1 or text.find('すき') > -1 or text.find('かわいい') > -1 or text.find('可愛い') > -1:
                    msg = 'えへへ'
                elif text.find('嫌い') > -1 or text.find('きらい') > -1:
                    msg = 'えへへ'
                elif text.find('月曜日が') > -1:
                    msg = '.........始マンディ！！！！！！:crescent_moon:'
                elif text.find('木曜日') > -1 or text.find('もくもく') > -1:
                    msg = 'もくもくもくようび〜\n'+kumo_san+'\n\n(・_・)ｽｯ\n\nなにがもくもくもくようびだ\n明日もまた仕事だぞ :cloud_lightning:'
                elif text.find('自己紹介') > -1:
                    msg = 'はい！はじめまして。クロレラさんに作られたヒヨッ子botの雲さんと申します。趣味は素数を数えることです。皆さんのお役に立てるようにがんばりますので、どうぞよろしくお願いします！:cloud:'
                elif text.find('help') > -1 or text.find('-h') > -1:
                    msg += 'https://discordapp.com/channels/XXXXXXXXXXXXXXXXXX/XXXXXXXXXXXXXXXXXX/XXXXXXXXXXXXXXXXXX'
                elif text.find('慰めて') > -1 or text.find('なぐさめて') > -1 or text.find('アドバイス') > -1 or text.find('助言') > -1:
                    msg = meigen.meigen()
                elif text.find('グー') > -1 or text.find('チョキ') > -1 or text.find('パー') > -1 or text.find('ぐー') > -1 or text.find('ちょき') > -1 or text.find('ぱー') > -1:
                    msg = keisuke_honda.keisuke_honda(text, user_id)
                elif text.find('なろう') > -1:
                    msg = narou.narou_search(text)
                elif text.find('犯罪係数') > -1 or text.find('ドミネータ') > -1 or text.find('サイコパス') > -1 or text.find('色相') > -1 or text.find('シビュラ') > -1:
                    msg = kumo_san + dominator.dominator(text)
                elif text.find('modokicraft') > -1:
                    msg += modokicraft.send_signal_to_modokicraft(text)
                elif text.find('wp') > -1:
                    msg = kumo_san + waruiko_point.waruiko_point(text, user_id)
                elif text.find('マインスイーパ') > -1 or text.find('まいんすいーぱ') > -1:
                    msg += '出題！\n' + minesweeper.minesweeper(text)
                elif text.find('級') > -1 or text.find('遊ぼ') > -1 or text.find('遊んで') > -1 or text.find('あそぼ') > -1 or text.find('あそんで') > -1:
                    msg += 'マインスイーパーしましょう！\n' + minesweeper.minesweeper(text)
                elif text.find('座') > -1:
                    msg += uranai.uranai(text)
                elif text.find('d') > -1:
                    msg += 'のダイス結果です\n' + dice.nDn(text)
                elif text.find('って何') > -1 or text.find('ってなに') > -1:
                    msg += wiki.wikipedia_search(text)
                elif text.find('天気') > -1:
                    msg += weather.get_weather_information(text)
                elif text.find('は素数') > -1:
                    msg += primarity_test.primarity_test(text, 50)
                ######## clear in #暴風域 ########
                elif text.find('おそうじ') > -1 or text.find('お掃除') > -1:
                    history = ""
                    if channel == client.get_channel(XXXXXXXXXXXXXXXXXX):
                        async for i in channel.history(oldest_first=True):
                            history += i.author.display_name+" "+i.content+"\n"
                        date = datetime.datetime.today().strftime("%Y_%m_%d")
                        path = 'removed_chat_logs/'+ date +'.txt'
                        if os.path.isfile(path) == False:
                            with open(path, mode='w') as f:
                                f.write(history)
                        else:
                            with open(path, mode='a') as f:
                                f.write(history)
                        await channel.purge()
                        msg += '塵一つ残しません！ :cloud_tornado: '
                    else:
                        msg += 'このコマンドは #暴風域 でしか使えないよ！'
                ###########################################
                else:
                    msg += 'その言葉は知らなかったから調べたよ。\n' + wiki.wiki(text)
                    #メッセージが送られてきたチャンネルへメッセージを送ります
                await channel.send(msg)
                return msg
            except Exception as e:
                print(e)
                raise e

client.run(token.token())
