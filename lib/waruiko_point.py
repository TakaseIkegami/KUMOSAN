import os
import re

# Count Waruiko Points
def waruiko_point(text, user_id):
    response_string = ''
    index_st = text.find('wp ')+3
    index_ed = text.find(' <@')
    index_st2 = text.find(' <@')+1
    index_ed2 = text.find('>')
    target = text[index_st2:index_ed2]
    target = re.sub('[<@!>/g]', "", target);
    print("target: " + target)
    path = 'users/'+target+".txt"
    if os.path.isfile(path) == False:
        with open(path, mode='w') as f:
            f.write(str(0))
    if text.find('-s') > -1 or text.find('--show') > -1:
        with open(path) as f:
            s = f.read()
            s = int(s)
            response_string = "現在の <@" + target + "> さんの悪い子ポイントは **"+ str(s) +"** ポイントです。"
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
    response_string = '悪い子ポイントを **' + text[index_st:index_ed] + '** しました。\nこれで <@' + target  + '> さんの悪い子ポイントは **'+str(s)+'** ポイントです。'
    return response_string

