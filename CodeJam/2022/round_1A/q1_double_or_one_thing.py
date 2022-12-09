def read_input():
    n = int(input())
    for _ in range(n):
        yield input()


def get_answer(s):
    repeat_char = s[0]
    repeat_count = 0

    result = ''

    for next_char in s:
        if next_char == repeat_char:
            repeat_count += 1
        else:
            if next_char > repeat_char:
                result += repeat_char*repeat_count
            repeat_char = next_char
            repeat_count = 1
            
        result += next_char

    return result;


if __name__ == '__main__':
    for i, test_case in enumerate(read_input()):
        res = get_answer(test_case)
        print(f'Case #{i + 1}: {res}')