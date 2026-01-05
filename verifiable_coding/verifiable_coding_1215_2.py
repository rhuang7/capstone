import sys

def solve():
    import sys
    from collections import defaultdict

    data = sys.stdin.buffer.read().split(b'\n')
    N = int(data[0])
    words = data[1:N+1]
    result = data[N+1].decode().strip()

    unique_chars = set()
    for word in words + [result]:
        unique_chars.update(word)
    unique_chars = list(unique_chars)
    if len(unique_chars) > 10:
        print("false")
        return

    char_to_digit = {}
    used_digits = set()

    def is_valid(word, digit_map):
        if len(word) > len(digit_map):
            return False
        for i in range(len(word)):
            c = word[i]
            if c in digit_map:
                if digit_map[c] != i:
                    return False
            else:
                return False
        return True

    def assign_digits(chars, digits):
        if not chars:
            return {}
        c = chars[0]
        for d in digits:
            if d not in used_digits:
                used_digits.add(d)
                char_to_digit[c] = d
                if is_valid(c, char_to_digit):
                    remaining = chars[1:]
                    remaining_digits = [d for d in digits if d != used_digits]
                    if assign_digits(remaining, remaining_digits):
                        return char_to_digit
                used_digits.remove(d)
        return None

    digits = [str(i) for i in range(10)]
    chars = unique_chars
    if assign_digits(chars, digits) is None:
        print("false")
        return

    total = 0
    for word in words:
        num = 0
        for c in word:
            num = num * 10 + int(char_to_digit[c])
        total += num

    res = 0
    for c in result:
        res = res * 10 + int(char_to_digit[c])

    if total == res:
        print("true")
    else:
        print("false")

if __name__ == '__main__':
    solve()