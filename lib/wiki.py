import wikipedia

# Search from Wikipedia
## Patter A
def wikipedia_search(text):
    response_string = ''
    wikipedia.set_lang('ja')
    index_st = text.find(' ')+1
    index_ed = text.find('って')
    search_text = text[index_st:index_ed]
    print(search_text)
    search_response = wikipedia.search(search_text)
    print(search_response)
    if len(search_response) > 0:
        try:
            wiki_page = wikipedia.page(search_response[0])
        except Exception as e:
            try:
                wiki_page = wikipedia.page(search_response[1])
            except Exception as e:
                response_string = 'お探しの言葉ではエラーを起こしました！:cold_sweat:\n' + e.message + '\n' + str(e)
        response_string = '説明しましょう！\n'
        response_string += wiki_page.content[0:200] + '.....\n'
        response_string += wiki_page.url
    else:
        response_string = '今はまだ見つけられません…でも頑張って見つけられるようになりますよー！'

    return response_string

## Pattern B
def wiki(text):
    response_string = ''
    wikipedia.set_lang('ja')
    index_st = text.find('雲さん ')+4
    #index_ed = text.find('')
    search_text = text[index_st:]
    print(search_text)
    search_response = wikipedia.search(search_text)
    print(search_response)
    if len(search_response) > 0:
        try:
            wiki_page = wikipedia.page(search_response[0])
        except Exception as e:
            try:
                wiki_page = wikipedia.page(search_response[1])
            except Exception as e:
                response_string = 'お探しの言葉ではエラーを起こしました！:cold_sweat:\n' + e.message + '\n' + str(e)
        response_string = '説明しよう！\n'
        response_string += wiki_page.content[0:200] + '.....\n'
        response_string += wiki_page.url
    else:
        response_string = '今はまだ見つけられません…でも頑張って見つけられるようになりますよー！'

    return response_string
