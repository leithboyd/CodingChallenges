def read_input():
    n = int(input())
    for _ in range(n):
        yield tuple(int(v) for v in input().split(' '))


if __name__ == '__main__':
    for i, (r, c) in enumerate(read_input()):

        print(f'Case #{i + 1}:')

        row0 = '-'.join('+'*(c + 1))
        row1 = '.'.join('|'*(c + 1))

        print('..' + row0[2:])
        print('..' + row1[2:])

        for ri in range(2, r*2 + 1):
            row = row0 if ri % 2 == 0 else row1
            print(row)