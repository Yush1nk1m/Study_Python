min_seat = 2
max_seat = 10
all_people = 100
memo = {}
def question(left, seat) :
    key = str([left, seat]) # "남은 사람 수, 앉은 사람 수" : count
    # 종료 조건
    if key in memo :
        return memo[key] # 카운트 값 반환 => count += 반환값
    if left < 0 :
        return 0 # => count += 0(변화 X)
    if left == 0 :
        return 1 # => count += 1(유일해)
    count = 0
    for i in range(seat, max_seat + 1) :
        count += question(left - i, i)
    memo[key] = count
    return count

print(question(all_people, min_seat))