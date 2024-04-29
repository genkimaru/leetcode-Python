n = input()
target = []
for i in range(int(n)):
    target.append(input())

t = list(map(lambda x : int(x) , target))
unique_t = set(t)
# print('result:')
for i in sorted(unique_t):
    print(i)