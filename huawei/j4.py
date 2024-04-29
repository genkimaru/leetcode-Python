str = input()
if not str:
    exit()
result = []
# range 和 slice 都是属于含头不含尾
for i in range(0, len(str) , 8):
    if i + 8 > len(str) -1 :
        s = str[i : len(str)] + '0'*( 8 - (len(str) - i ))
    else:
        s = str[i:i+8]
    result.append(s)
for i in result:
    print(i)
    