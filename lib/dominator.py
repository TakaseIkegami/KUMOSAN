import random
import datetime

# Dominator
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

