a = [1, 584, 4, 6, 11]
b = [5, 8, 6, 12, 4]
c = []
for i in a:
    for j in b:
        if i == j:
            c.append(i)

print(c)
