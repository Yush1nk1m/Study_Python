key_list = ['name', 'hp', 'mp', 'level']
value_list = ['기사', 200, 30, 5]
character = {}

i = 0
while i < len(key_list) :
    character[key_list[i]] = value_list[i]
    i += 1

# 최종 출력
print(character)