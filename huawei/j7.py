num = int(input())
d = {}
for i in range(num):
    aa , bb = input().split()
    a , b = int(aa), int(bb)
    if a in d:
        d[a] = d[a] + b
    else:
        d[a] = b

## 对字典排序的方式。
d = dict(sorted(d.items()))
for i , j in d.items():
    print(i  ,j)