# 딕셔너리를 선언합니다.
character = {
    'name' : '기사',
    'level' : 12,
    'items' : {
        'sword' : '불꽃의 검',
        'armor' : '풀플레이트'
    },
    'skill' : ['베기', '세게 베기', '아주 세게 베기']
}

# for 반복문을 사용합니다.
for key in character :
    if type(character[key]) is list :
        for element in character[key] :
            print('{} : {}'.format(key, element))
    elif type(character[key]) is dict :
        for item in character[key] :
            print('{} : {}'.format(item, character[key][item]))
    else :
        print('{} : {}'.format(key, character[key]))