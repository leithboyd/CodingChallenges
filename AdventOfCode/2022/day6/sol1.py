# https://adventofcode.com/2022/day/6

message = open('./day6/input.txt', 'r').read()


def solve(message: str, unique_sequence_length: int, verbose=False):
    last_seen=[0]*26

    start_i = 0
    for i, c in enumerate(ord(c) - ord('z') for c in message):
        if verbose:
            print(message[start_i: i + 1])
        if last_seen[c] >= start_i:
            # the character already exists in the current sequence
            # advance the start of the sequence to remove the conflict
            start_i = last_seen[c] + 1
        elif i - start_i + 1 == unique_sequence_length:
            # the sequence has no conflicts and is of the correct length
            break

        last_seen[c] = i

    return i + 1


print(solve(message, 4))
