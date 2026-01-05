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

    # Find all unique characters
    all_chars = list(unique_chars)
    for c in all_chars:
        if c.isalpha():
            char_to_digit[c] = None

    # Try all possible digit assignments
    from itertools import permutations

    for digits in permutations(range(10), len(char_to_digit)):
        mapping = dict(zip(char_to_digit, digits))
        valid = True
        for word in words:
            total = 0
            for c in word:
                if c in mapping:
                    total = total * 10 + mapping[c]
                else:
                    valid = False
                    break
            if not valid:
                break
        if not valid:
            continue

        # Check result
        total_result = 0
        for c in result:
            if c in mapping:
                total_result = total_result * 10 + mapping[c]
            else:
                valid = False
                break
        if not valid:
            continue

        # Check if total of words equals result
        total_words = 0
        for word in words:
            total = 0
            for c in word:
                total = total * 10 + mapping[c]
            total_words = total_words * 10 + total
        if total_words == total_result:
            print("true")
            return

    print("false")

if __name__ == '__main__':
    solve()