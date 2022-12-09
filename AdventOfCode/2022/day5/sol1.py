
import re

raw_input = open('./day5/input.txt').read().splitlines()

input_split = raw_input.index('')

n_stacks = len([c for c in raw_input[input_split - 1].split(' ') if c])

def parse_stacks(raw_stacks_input, n_stacks):
    stacks = [[] for _ in range(n_stacks)]

    regexp = re.compile(r'[ \[](.)[ \]]')

    for line in reversed(raw_stacks_input):
        for i, m in enumerate(regexp.findall(line)):
            if not m.isspace():
                stacks[i].append(m)

    return stacks


def parse_operations(raw_operations_input):
    regexp = re.compile('^move ([^ ]+) from ([^ ]+) to ([^ ]+)$')

    return [tuple(map(int,regexp.match(line).groups())) for line in raw_operations_input]


stacks = parse_stacks(raw_input[: input_split - 1], n_stacks)
operations = parse_operations(raw_input[input_split + 1 :])


for n, orig_i, dest_i in operations:
    orig = stacks[orig_i-1]
    dest = stacks[dest_i-1]
    
    for i in range(n):
        dest.append(orig.pop())

print(''.join(s[-1] for s in stacks))