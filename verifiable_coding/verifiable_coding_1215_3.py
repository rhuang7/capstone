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

    # Extract all unique characters
    all_chars = list(unique_chars)
    for c in all_chars:
        if c.isdigit():
            char_to_digit[c] = int(c)
            used_digits.add(int(c))

    # Check if all characters in result are digits
    for c in result:
        if not c.isdigit():
            print("false")
            return

    # Check if all characters in words are unique or digits
    for word in words:
        for c in word:
            if not (c.isdigit() or c in char_to_digit):
                print("false")
                return

    # Try all possible digit assignments
    from itertools import permutations

    # Get all unique characters that are not digits
    non_digit_chars = [c for c in all_chars if not c.isdigit()]
    if len(non_digit_chars) > 10:
        print("false")
        return

    # Try all possible digit assignments for non-digit characters
    for perm in permutations(range(10), len(non_digit_chars)):
        char_to_digit = {}
        for i, c in enumerate(non_digit_chars):
            char_to_digit[c] = perm[i]
        used_digits = set(perm)

        # Check if any digit is already used
        for c in char_to_digit.values():
            if c in used_digits:
                print("false")
                break
        else:
            # Check if any word starts with 0
            for word in words:
                if word[0] in char_to_digit and char_to_digit[word[0]] == 0:
                    print("false")
                    break
            else:
                # Check if result starts with 0
                if result[0] in char_to_digit and char_to_digit[result[0]] == 0:
                    print("false")
                    continue

                # Convert words and result to numbers
                try:
                    word_values = [int(''.join(str(char_to_digit[c]) for c in word)) for word in words]
                    result_value = int(''.join(str(char_to_digit[c]) for c in result))
                except:
                    print("false")
                    continue

                # Check if sum of words equals result
                if sum(word_values) == result_value:
                    print("true")
                    return

    print("false")

if __name__ == '__main__':
    solve()