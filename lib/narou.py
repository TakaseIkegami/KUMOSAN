import requests
import json

# Narou
def narou_search(text):
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

