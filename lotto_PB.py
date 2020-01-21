import random


n = []


for x in range(6):


    if x < 5:
        r = random.randint(1,69)
        n.append(r)


    else:
        r = random.randint(1,26)
        n.append(r)


print(n)
