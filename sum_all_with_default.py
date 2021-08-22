# 함수를 선언합니다.
def sum_all(start = 0, end = 100, step = 1) :
    output = 0
    for i in range(start, end + 1, step) :
        output += i
    # 리턴합니다.
    return output

# 함수를 호출합니다.
print("A.", sum_all(0, 100, 10))
print("B.", sum_all(end = 100))
print("C.", sum_all(end = 100, step = 2))