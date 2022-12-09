
raw_input = open('./day4/input.txt', 'r').read().splitlines()

def parse_range_pair(s):
    return tuple(tuple(map(int, pair_part.split('-'))) for pair_part in s.split(','))


pairs = [parse_range_pair(line) for line in raw_input]


def contains(r1, r2):
    # test if r1 contains r2
    # r1 |        |
    # r2     |   |
    return  r1[0] <= r2[0] and r2[1] <= r1[1] 


def any_contains(r1, r2):
    # test if r1 contains r2 OR r2 contains r1
    return contains(r1, r2) or contains(r2, r1) 



print(sum(any_contains(*p) for p in pairs))