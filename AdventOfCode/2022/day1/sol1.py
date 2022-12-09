max_total = -1

with open('./day1/input.txt', 'r') as f:
    total = 0
    for l in f.readlines():
        l = l.strip()
        if not l:
            max_total = max(max_total, total)
            total = 0
        else:
            total += int(l)
        
    max_total = max(max_total, total)


print(max_total)