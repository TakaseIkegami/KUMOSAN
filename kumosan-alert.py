# サーバで何かしらの処理を行っているとき、処理が終了したことを雲さんがdiscordで教えてくれるスクリプト
# $ FCrackzip hoge.zip && python kumosan-alert.py とかって使う

import discord
import sys

client = discord.Client()
args = sys.argv
main_chat='任意のチャンネルid'
bot_salon='任意のチャンネルid'
selector = bot_salon
print(args)

if args[1] == "bot":
    selector = bot_salon
elif args[1] == "main":
    selector = main_chat
else:
    selector = bot_salon
print(selector)

#@client.event
#async def on_ready():
#    print('Logged in as')
#    print(client.user.name)
#    print(client.user.id)
#    print('------')

################# Don't touch. ################
kumo_san = '╭◜◝ ͡ ◜◝╮ \n(   •ω•　  ) \n╰◟◞ ͜ ◟◞╯ < '
################# Don't touch. ################


channel = client.get_channel(selector)
txt = "Takaseさん、解読が終わりました！"
msg = kumo_san + txt
print(msg)
await client.send_message(channel, msg)

client.run("ここにトークンを書いてね")
