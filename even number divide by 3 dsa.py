count = 0
num =2
while True:
    if num %6!=  0:
        num+= 2
        continue
    print(num)
    count+=  1
    num+= 2
    if count == 50:
        break
