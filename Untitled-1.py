a = []
for i in range(100):
    if i % 2 != 0 and i % 3 == 2:
        a.append(i)

print(min(a))
