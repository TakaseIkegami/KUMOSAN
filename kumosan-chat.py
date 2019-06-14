# コマンドラインから雲さんでコメントを投げるスクリプト
# (引数の指定でチャンネルを選択できます)

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


@client.event
async def on_ready():
    ################# Don't touch. ################
    kumo_san = '╭◜◝ ͡ ◜◝╮ \n(   •ω•　  ) \n╰◟◞ ͜ ◟◞╯ < '
    ################# Don't touch. ################
    channel = client.get_channel(selector)
    while True:
        txt = input()
        msg = kumo_san + txt
        print(msg)
        await client.send_message(channel, msg)
    return msg

client.run("ここにトークンを書いてね")
