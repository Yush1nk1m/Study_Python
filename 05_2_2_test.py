앉힐수있는최소사람수 = 2
앉힐수있는최대사람수 = 10
전체사람의수 = 100
memo = {}

# 트리 : 노드에 적은 값 / 엣지에 적은 값
def 문제(남은사람수, 앉힌사람수) :
    key = str((남은사람수, 앉힌사람수))
    # 종료 조건
    if key in memo :
        return memo[key]
    if 남은사람수 < 0 :
        return 0 # 무효하니 0을 리턴
    if 남은사람수 == 0 :
        return 1 # 유효하니 수를 세면 돼서 1을 리턴
    # 재귀 호출
    # 2~10 => 이전 엣지에 쓰여진 ~ 10
    count = 0
    for i in range(앉힌사람수, 앉힐수있는최대사람수 + 1) :
        count += 문제(남은사람수 - i, i)
    # 메모화 처리
    memo[key] = count
    return count

print(문제(전체사람의수, 앉힐수있는최소사람수))