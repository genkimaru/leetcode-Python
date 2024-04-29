num = int(input())

factors = []
divisor = 2

while divisor * divisor  <= num :
    if num % divisor == 0:
        factors.append(divisor)
        num = num // divisor
    else:
        if divisor == 2:
            divisor = 3
        else:
            divisor += 2
if num > 1:
    factors.append(num)


print(" ".join(map(str, factors)))