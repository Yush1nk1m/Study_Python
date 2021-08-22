from primePy import primes

number = 0
primelist = []
for i in range(100, 1000 + 1) :
    if primes.check(i) == True :
        primelist.append(i)
        number += 1
    else :
        continue
print(primelist)
print("100과 1000사이에 있는 소수의 개수 : {}개".format(number))