str = input('please input ')
count = 0
for i in reversed(str):
    if i == ' ':
        break
    count += 1

print(count)