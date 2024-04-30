# input money and count
money , count = map(int , input().split())

t = []
for i in range(count):
    price , prio , main = map( int , input().split())
    t.append((price , prio , main))

# price * prio

