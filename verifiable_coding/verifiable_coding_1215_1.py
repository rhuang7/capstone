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
        if c not in char_to_digit:
            char_to_digit[c] = None

    # Try all possible digit assignments
    from itertools import permutations

    for digits in permutations(range(10), len(all_chars)):
        mapping = dict(zip(all_chars, digits))
        # Check if any character is mapped to 0 and is the first character of a word
        for word in words + [result]:
            if word[0] in mapping and mapping[word[0]] == 0:
                break
        else:
            # Check if the mapping is valid
            valid = True
            for word in words:
                total = 0
                for c in word:
                    total = total * 10 + mapping[c]
                if total < 0 or total > 10**10:
                    valid = False
                    break
            if not valid:
                continue
            # Check if the sum of words equals the result
            total = 0
            for word in words:
                total = total * 10 + mapping[word[0]]
                for c in word[1:]:
                    total = total * 10 + mapping[c]
            res = 0
            for c in result:
                res = res * 10 + mapping[c]
            if total == res:
                print("true")
                return
    print("false")

if __name__ == '__main__':
    solve()