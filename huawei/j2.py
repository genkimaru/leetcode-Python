str = input()
c = input()
target =  []
if ord(c) >= ord('a') and ord(c) <= ord('z'):
    target = [ c, chr(ord(c) - 32)]
elif ord(c) >= ord('A') and ord(c) <= ord('Z'):
    target = [ c, chr(ord(c) + 32)]
else:
    target = [c]

count = 0
for i in str:
    if i in target:
        count += 1

print(count)
