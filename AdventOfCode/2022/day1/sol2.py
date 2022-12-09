totals = []

with open('./day1/input.txt', 'r') as f:
    total = 0
    for l in f.readlines():
        l = l.strip()
        if not l:
            totals.append(total)
            total = 0
        else:
            total += int(l)
        
    totals.append(total)

answer = sum(sorted(totals, reverse=True)[:3])

print(answer)