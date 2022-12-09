# https://adventofcode.com/2022/day/3

input = open('./day3/input.txt', 'r').read().splitlines()


def get_common_element(s):
    halfway = len(s)//2

    compartment1 = set(s[:halfway])
    compartment2 = set(s[halfway:])

    return compartment1.intersection(compartment2).pop()


char_value = {**{chr(ord('a') + i): i + 1 for i in range(0, 26)},
              **{chr(ord('A') + i): i + 27 for i in range(0, 26)}}

print(sum(map(lambda i: char_value[get_common_element(i)], input)))