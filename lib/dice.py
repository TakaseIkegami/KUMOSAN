import random
import re

def judge_nDn(src, pattern):
    repatter = re.compile(pattern)
    result = repatter.fullmatch(src)
    if result is not None:
        return True
    else:
        return False

# 何面ダイスを何回振るか
def split_nDn(src, split_pattern):
    return re.split(split_pattern,src)

# ダイスを振る
def role_nDn(src, split_pattern):
    result = []
    sum_dice = 0
    role_index = split_nDn(src, split_pattern)
    role_count = int(role_index[0])
    nDice = int(role_index[1])

    for i in range(role_count):
        tmp = random.randint(1,nDice)
        result.append(tmp)
        sum_dice = sum_dice + tmp

    is1dice = True if role_count == 1 else False

    return result,sum_dice,is1dice

def nDn(text):
    pattern = '\d{1,2}d\d{1,3}|\d{1,2}D\d{1,3}'
    split_pattern = 'd|D'
    index_st = text.find('雲さん ')+4
    search_text = text[index_st:]
    if judge_nDn(search_text, pattern):
        result,sum_dice,is1dice = role_nDn(search_text, split_pattern)
        if is1dice:
            response_string = 'ｺﾛﾝ… **`' + str(sum_dice) + '`**'
            return response_string
        else:
            response_string = 'ｼﾞｬﾗｼﾞｬﾗｼﾞｬﾗ… **`' + str(result) + '`** = **`' + str(sum_dice) + '`**'
            return response_string
    else:
        return None

