def read_input():
    n = int(input())
    for _ in range(n):
        m, _ = [int(v) for v in input().split(' ')]

        yield [[int(v) for v in input().split(' ')] for _ in range(m)]


def get_solution(test_case):
    val1, sol1 = 0, 0
    val2, sol2 = 0, 0 

    for lo, hi in [(min(v), max(v)) for v in test_case]:
        distance = hi - lo

        sol1_new = min(sol1 + abs(lo - val1), sol2 + abs(lo - val2)) + distance
        sol2_new = min(sol1 + abs(hi - val1), sol2 + abs(hi - val2)) + distance

        sol1 = sol1_new
        val1 = hi

        sol2 = sol2_new
        val2 = lo
        
    return min(sol1,  sol2)

if __name__ == '__main__':
    for i, test_case in enumerate(read_input()):
        print(f'Case #{i+1}: {get_solution(test_case)}')




