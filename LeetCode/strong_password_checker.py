# Problem: https://leetcode.com/problems/strong-password-checker/

def repeated_character_counts(s: str, n: int):
    repeated_char = None
    count = 0
    for c in s:
        if c == repeated_char:
            count += 1
        else:
            if count >= n:
                yield count
            repeated_char = c
            count = 1
    
    if count >= n:
        yield count


def apply_delete_operations(n: int, character_groups: list[int]) -> list[int]:
    def apply_deletes(v):
        nonlocal n
        to_remove = v - 2 if v % 3 == 2 else v % 3 + 1
        can_remove = min(to_remove, n)
        n -= can_remove
        return v - can_remove

    character_groups.sort(key=lambda x: x % 3)
    character_groups = [v for v in map(apply_deletes, character_groups) if v >= 3]
    character_groups = [v for v in map(apply_deletes, character_groups) if v >= 3]
    return character_groups


class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        character_group_sizes = list(repeated_character_counts(password, 3))
        min_combined_insert_replace = 3 - (has_upper + has_lower + has_digit)
        
        inserts = 0
        deletes = 0
        replaces = 0

        length = len(password)
        if length > 20:
            character_group_sizes = apply_delete_operations(length-20, character_group_sizes)
            deletes += length-20
        elif length < 6:
            if character_group_sizes and character_group_sizes[0] == 5:
                character_group_sizes[0] = 3
            else:
                character_group_sizes = []
            inserts += 6 - length

        replaces += sum(count // 3 for count in character_group_sizes)

        if inserts + replaces < min_combined_insert_replace:
            replaces += min_combined_insert_replace - (inserts + replaces)

        return inserts + deletes + replaces


if __name__ == '__main__':

    sol = Solution()
    print(sol.strongPasswordChecker('aaaaaabccccccdeeeeeefgggggg'))
    print(sol.strongPasswordChecker('a'))
    print(sol.strongPasswordChecker('aA1'))
    print(sol.strongPasswordChecker('1337C0d3'))
