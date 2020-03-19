import requests
import json

# Get Weather Infomation
# Special Thanks: @black_ichigo153
def get_weather_information(text):
    weather_api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
    response_string = ''
    city_id = ''
    if text.find('長野') > -1:
        city_id = '200010'
    elif text.find('松本') > -1:
        city_id = '200020'
    elif text.find('伊那') > -1:
        city_id = '200030'
    elif text.find('新潟') > -1:
        city_id = '150010'
    elif text.find('富山') > -1:
        city_id = '160010'
    elif text.find('石川') > -1:
        city_id = '170010'
    elif text.find('福井') > -1:
        city_id = '180010'
    elif text.find('岐阜') > -1:
        city_id = '210010'
    elif text.find('三重') > -1:
        city_id = '240010'
    elif text.find('青森') > -1:
        city_id = '020010'
    elif text.find('大阪') > -1:
        city_id = '270000'
    elif text.find('兵庫') > -1 or text.find('神戸') > -1:
        city_id = '280010'
    elif text.find('京都') > -1:
        city_id = '260010'
    elif text.find('滋賀') > -1:
        city_id = '250010'
    elif text.find('和歌山') > -1:
        city_id = '300010'
    elif text.find('奈良') > -1:
        city_id = '290010'
    elif text.find('十津川') > -1:
        city_id = '290020'
    elif text.find('鳥取') > -1:
        city_id = '310010'
    elif text.find('島根') > -1:
        city_id = '320010'
    elif text.find('広島') > -1:
        city_id = '340010'
    elif text.find('岡山') > -1:
        city_id = '330010'
    elif text.find('山口') > -1:
        city_id = '350010'
    elif text.find('徳島') > -1:
        city_id = '360010'
    elif text.find('香川') > -1:
        city_id = '370000'
    elif text.find('愛媛') > -1:
        city_id = '380010'
    elif text.find('高知') > -1:
        city_id = '390010'
    elif text.find('東京') > -1:
        city_id = '130010'
    elif text.find('埼玉') > -1 or text.find('電大') > -1 or text.find('鳩山') > -1 or text.find('熊谷') > -1 or text.find('大学') > -1:
        city_id = '110020'
    elif text.find('千葉') > -1:
        city_id = '120010'
    elif text.find('茨城') > -1:
        city_id = '080010'
    elif text.find('栃木') > -1:
        city_id = '090010'
    elif text.find('群馬') > -1:
        city_id = '100010'
    elif text.find('山梨') > -1:
        city_id = '190010'
    elif text.find('神奈川') > -1 or text.find('横浜') > -1:
        city_id = '140010'
    elif text.find('岩手') > -1:
        city_id = '030010'
    elif text.find('宮城') > -1:
        city_id = '040010'
    elif text.find('秋田') > -1:
        city_id = '050010'
    elif text.find('山形') > -1:
        city_id = '060010'
    elif text.find('福島') > -1:
        city_id = '070010'
    elif text.find('北海道') > -1 or text.find('道央') > -1 or text.find('札幌') > -1:
        city_id = '016010'
    elif text.find('道北') > -1 or text.find('旭川') > -1:
        city_id = '011000'
    elif text.find('道南') > -1 or text.find('室蘭') > -1:
        city_id = '015010'
    elif text.find('道東') > -1 or text.find('網走') > -1:
        city_id = '013010'
    elif text.find('愛知') > -1 or text.find('名古屋') > -1:
        city_id = '230010'
    elif text.find('静岡') > -1:
        city_id = '220010'
    elif text.find('福岡') > -1 or text.find('九州') > -1:
        city_id = '400010'
    elif text.find('大分') > -1:
        city_id = '440010'
    elif text.find('長崎') > -1:
        city_id = '420010'
    elif text.find('宮崎') > -1:
        city_id = '450010'
    elif text.find('鹿児島') > -1:
        city_id = '460010'
    elif text.find('熊本') > -1:
        city_id = '430010'
    elif text.find('沖縄') > -1:
        city_id = '471010'
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

