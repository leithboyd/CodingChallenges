import numpy as np


def read_input():
    n = int(input())
    for _ in range(n):
        input()
        yield [int(v) for v in input().split(' ')]


if __name__ == '__main__':
    for i, test_case in enumerate(read_input()):
        test_case.sort()

        c = 0
        for v in test_case:
            if c + 1 <= v:
                c += 1

        print(f'Case #{i + 1}: {c}')
