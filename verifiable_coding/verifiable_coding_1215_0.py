import sys
import string

def solve():
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

    all_chars = list(unique_chars)
    for c in all_chars:
        if c in string.digits:
            char_to_digit[c] = int(c)
            used_digits.add(int(c))

    for word in words + [result]:
        for c in word:
            if c in char_to_digit:
                continue
            if c in string.digits:
                if int(c) in used_digits:
                    print("false")
                    return
                char_to_digit[c] = int(c)
                used_digits.add(int(c))
            else:
                pass

    for word in words + [result]:
        for c in word:
            if c in string.digits:
                continue
            if c not in char_to_digit:
                print("false")
                return

    for word in words:
        num = 0
        for c in word:
            num = num * 10 + char_to_digit[c]
        if num < 0 or num > 10**10:
            print("false")
            return

    total = 0
    for word in words:
        total += char_to_digit[word[0]] * (10 ** (len(word) - 1))
        for c in word[1:]:
            total += char_to_digit[c] * (10 ** (len(word) - 1 - word.index(c)))

    result_num = 0
    for c in result:
        result_num = result_num * 10 + char_to_digit[c]

    if total == result_num:
        print("true")
    else:
        print("false")

if __name__ == '__main__':
    solve()