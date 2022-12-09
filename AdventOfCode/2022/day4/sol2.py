
raw_input = open('./day4/input.txt', 'r').read().splitlines()

def parse_range_pair(s):
    return tuple(tuple(map(int, pair_part.split('-'))) for pair_part in s.split(','))


pairs = [parse_range_pair(line) for line in raw_input]


def overlap(r1, r2):
    # don't over lap cases
    # case 1:
    #  r1 |    |
    #  r2         |    |
    #
    # case 2:
    #  r1         |    |
    #  r2 |    |               
    #
    return not(r1[1] < r2[0] or r2[1] < r1[0])


print(sum(overlap(*p) for p in pairs))