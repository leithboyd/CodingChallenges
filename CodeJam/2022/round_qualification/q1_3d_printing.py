import numpy as np


def read_input():
    n = int(input())
    for _ in range(n):
        yield [[int(v) for v in input().split(' ')] for _ in range(3)]


if __name__ == '__main__':
    target = 10**6

    for i, test_case in enumerate(read_input()):
        available = np.array(test_case).min(axis=0)

        if available.sum() < target:
            answer=None
            answer_str = 'IMPOSSIBLE'
        else:
            remaining = np.maximum(target - np.cumsum(available), 0)
            remaining = np.roll(remaining, 1)
            remaining[0] = target

            answer = np.minimum(available, remaining)
            answer_str = ' '.join(map(str, answer))
            
        print(f"Case #{i+1}: {answer_str}")
