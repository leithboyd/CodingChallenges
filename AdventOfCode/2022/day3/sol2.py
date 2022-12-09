# https://adventofcode.com/2022/day/3

from functools import reduce

input = open('./day3/input.txt', 'r').read().splitlines()


def get_common_element(g):
    return reduce(lambda a,b: a.intersection(b), map(set, g)).pop()


char_value = {**{chr(ord('a') + i): i + 1 for i in range(0, 26)},
              **{chr(ord('A') + i): i + 27 for i in range(0, 26)}}

groups = zip(input[::3], input[1::3], input[2::3])

print(sum(char_value[get_common_element(g)] for g in groups))