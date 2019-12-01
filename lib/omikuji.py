import random

# Omikuji
def omikuji():
    response_string = ''
    lots = ["大吉", "吉", "中吉", "小吉", "半吉", "末吉", "末小吉", "平", "凶", "小凶", "半凶", "末凶", "大凶", "未分"]
    random.shuffle(lots)
    lot = lots[0]
    print(lot)
    response_string = "あなたの運勢は...ｶﾞｼｬｶﾞｼｬｶﾞｼｬｶﾞｼｬ...\n\n　　　　" + lot + "　ですね！"

    return response_string
