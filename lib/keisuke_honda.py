from . import waruiko_point
import random

# KeisukeHonda
def keisuke_honda(text, user_id):
    response_string = ''
    d100 = random.randint(1, 100)
    print(d100)
    if d100 <= 3:
        if text.find('グー') > -1 or text.find('ぐー') > -1:
            response_string = 'ちょき！'
        elif text.find('チョキ') > -1 or text.find('ちょき') > -1:
            response_string = 'ちょき！'
        elif text.find('パー') > -1 or text.find('ぱー') > -1:
            response_string = 'ぐー！'
        response_string += '\n :regional_indicator_y: :regional_indicator_o: :regional_indicator_u:  :regional_indicator_w: :regional_indicator_i: :regional_indicator_n:\n やるやん。明日ぼくにリベンジさせて。これあげる。\n\n wp -1 '+user_id+'\n'
        txt = '雲さん wp -1 <@' + user_id + '>'
        res = waruiko_point(txt, 0)
        response_string += res
    elif d100 > 3:
        if text.find('グー') > -1 or text.find('ぐー') > -1:
            response_string = 'ぱー！'
        elif text.find('チョキ') > -1 or text.find('ちょき') > -1:
            response_string = 'ぐー！'
        elif text.find('パー') > -1 or text.find('ぱー') > -1:
            response_string = 'ちょき！'
        if 3 < d100 <= 33:
            response_string += '\n :regional_indicator_y: :regional_indicator_o: :regional_indicator_u:  :regional_indicator_l: :regional_indicator_o: :regional_indicator_s: :regional_indicator_e:\n ぼくの勝ち。何で負けたか、明日までに考えといてください。そしたら何かが見えてくるはずです。'
        elif 33 < d100 <= 66:
            response_string += '\n :regional_indicator_y: :regional_indicator_o: :regional_indicator_u:  :regional_indicator_l: :regional_indicator_o: :regional_indicator_s: :regional_indicator_e:\n ぼくの勝ち。たかがじゃんけん、そう思ってないですか？それやったら明日も、ぼくが勝ちますよ。'
        elif 66 < d100 <= 100:
            response_string += '\n :regional_indicator_y: :regional_indicator_o: :regional_indicator_u:  :regional_indicator_l: :regional_indicator_o: :regional_indicator_s: :regional_indicator_e:\n ぼくの勝ち。負けは次に繋がるチャンスです。ねばーぎぶあっぷ！'
    else:
        response_string('@クロレラ#9240 さん、手が出ません。')
    return response_string
