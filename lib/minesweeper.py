import random

# Minesweeper
def minesweeper(text):
    response_string = ''
    if text.find('低級') > -1:
        difficulty = 0.1
        rows = 8
        clear_range = [3, 4]
        response_string += '[低級]'
    elif text.find('中級') > -1:
        difficulty = 0.15
        rows = 10
        clear_range = [3, 5]
        response_string += '[中級]'
    elif text.find('上級') > -1:
        difficulty = 0.2
        rows = 12
        clear_range = [4, 7]
        response_string += '[上級]'
    elif text.find('超級') > -1:
        difficulty = 0.25
        rows = 12
        clear_range = [4, 6]
        response_string += '[超級]'
    elif text.find('雲さん級') > -1:
        difficulty = 0.3
        rows = 12
        clear_range = [4, 6]
        response_string += '[雲さん級]'
    else:
        difficulty = 0.15
        rows = 10
        clear_range = [3, 5]
        response_string += '[中級]'
    response_string += '\n'
    # 盤面の初期化、および爆弾の設置(100)
    stage = [[100 if random.random()<difficulty else 0 for x in range(rows+1)] for y in range(rows+1)]

    # 爆弾を探索し、周辺マスをカウントアップ
    for x in range(rows):
        for y in range(rows):
            try:
                if stage[x][y] >= 100:
                    stage[x-1][y-1] += 1
                    stage[x][y-1]+=1
                    stage[x+1][y-1] += 1

                    stage[x-1][y] += 1
                    #stage[x][y] += 1
                    stage[x+1][y] += 1

                    stage[x-1][y+1] += 1
                    stage[x][y+1] += 1
                    stage[x+1][y+1] += 1
            except (IndexError) as e:
                pass

    # 伏せ字への変換
    for x in range(rows):
        for y in range(rows):
            if clear_range[0]<=x<=clear_range[1] and clear_range[0]<=y<=clear_range[1]:
                if stage[x][y] == 0:
                    stage[x][y] = ":zero:"
                elif stage[x][y] == 1:
                    stage[x][y] = ":one:"
                elif stage[x][y] == 2:
                    stage[x][y] = ":two:"
                elif stage[x][y] == 3:
                    stage[x][y] = ":three:"
                elif stage[x][y] == 4:
                    stage[x][y] = ":four:"
                elif stage[x][y] == 5:
                    stage[x][y] = ":five:"
                elif stage[x][y] == 6:
                    stage[x][y] = ":six:"
                elif stage[x][y] == 7:
                    stage[x][y] = ":seven:"
                elif stage[x][y] == 8:
                    stage[x][y] = ":eight:"
                elif stage[x][y] >= 100:
                    stage[x][y] = "||:bomb:||"
            else:
                if stage[x][y] >= 100:
                    stage[x][y] = "||:bomb:||"
                elif stage[x][y] == 0:
                    stage[x][y] = "||:zero:||"
                elif stage[x][y] == 1:
                    stage[x][y] = "||:one:||"
                elif stage[x][y] == 2:
                    stage[x][y] = "||:two:||"
                elif stage[x][y] == 3:
                    stage[x][y] = "||:three:||"
                elif stage[x][y] == 4:
                    stage[x][y] = "||:four:||"
                elif stage[x][y] == 5:
                    stage[x][y] = "||:five:||"
                elif stage[x][y] == 6:
                    stage[x][y] = "||:six:||"
                elif stage[x][y] == 7:
                    stage[x][y] = "||:seven:||"
                elif stage[x][y] == 8:
                    stage[x][y] = "||:eight:||"
                elif 9 <= stage[x][y] < 100:
                    return minesweeper(text)
            response_string += str(stage[x][y])
        response_string += "\n"
    return response_string

