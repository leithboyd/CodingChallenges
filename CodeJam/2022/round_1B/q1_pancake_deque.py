def read_input():
    n = int(input())
    for _ in range(n):
        _ = input()
        yield [int(v) for v in input().split(' ')]


def min_from_ends(arr):
    i_start, i_end = 0, len(arr) - 1

    while i_start <= i_end:
        start, end = arr[i_start], arr[i_end]

        if start <= end:
            yield start
            i_start += 1
        else:
            yield end
            i_end -= 1


def get_solution(deque):
    threshold = 0

    count = 0
    for v in min_from_ends(deque):
        if v >= threshold:
            count += 1
            threshold = v

    return count


if __name__ == '__main__':
    for i, test_case in enumerate(read_input()):
        print(f'Case #{i+1}: {get_solution(test_case)}')