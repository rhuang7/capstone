import sys

def solve():
    import sys
    from collections import defaultdict

    data = sys.stdin.buffer.read().split()
    N = int(data[0])
    words = data[1:N+1]
    result = data[N+1]

    unique_chars = set()
    for word in words + [result]:
        unique_chars.update(word)
    if len(unique_chars) > 10:
        print("false")
        return

    char_to_digit = {}
    used_digits = set()

    def is_valid(word, value):
        if len(word) != len(str(value)):
            return False
        for c, d in zip(word, str(value)):
            if c in char_to_digit:
                if char_to_digit[c] != int(d):
                    return False
            else:
                if d in used_digits:
                    return False
                char_to_digit[c] = int(d)
                used_digits.add(d)
        return True

    def backtrack(remaining_chars, used_digits, char_to_digit, words, result):
        if not remaining_chars:
            return is_valid(result, sum(char_to_digit[c] * 10**(len(result) - 1 - i) for i, c in enumerate(result)))
        for c in remaining_chars:
            if c in char_to_digit:
                continue
            for d in range(10):
                if d in used_digits:
                    continue
                char_to_digit[c] = d
                used_digits.add(d)
                if backtrack(remaining_chars - {c}, used_digits, char_to_digit, words, result):
                    return True
                used_digits.remove(d)
                del char_to_digit[c]
        return False

    remaining_chars = set(unique_chars)
    if backtrack(remaining_chars, set(), {}, words, result):
        print("true")
    else:
        print("false")

if __name__ == '__main__':
    solve()