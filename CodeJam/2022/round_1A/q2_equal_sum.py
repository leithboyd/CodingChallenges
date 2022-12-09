import sys

# python .\interactive_runner.py python3 .\round_1A\q2_local_testing_tool.py 0 -- python3 .\round_1A\q2_equal_sum.py

def get_solution(power_2, other):
    partition = []
    partition_sum = 0
    other_partition_sum = 0

    for v in (*other, *reversed(power_2)):
        if partition_sum < other_partition_sum:
            partition_sum += v
            partition.append(v)
        else:
            other_partition_sum += v

    return partition


if __name__ == '__main__':
    test_cases = int(input())

    output_2 = [2**i for i in range(30)]
    output_other = [256 + (i + 1) for i in range(70)]
    output = ' '.join(map(str, (*output_2, *output_other)))

    for i in range(test_cases):
        N = int(input())
        print(output)
        solution = get_solution([*output_2],  [*(int(v) for v in input().split(' ')), *output_other])
        solution_str = ' '.join(map(str, solution))
        print(solution_str)
    
