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
            if word[i] in digit_map:
                if digit_map[word[i]] != i:
                    return False
            else:
                return False
        return True

    def backtrack(index, used_digits, char_to_digit, unique_chars, words, result):
        if index == len(unique_chars):
            return check(words, result, char_to_digit)
        char = unique_chars[index]
        for d in range(10):
            if d in used_digits:
                continue
            char_to_digit[char] = d
            used_digits.add(d)
            if backtrack(index + 1, used_digits, char_to_digit, unique_chars, words, result):
                return True
            used_digits.remove(d)
            del char_to_digit[char]
        return False

    def check(words, result, char_to_digit):
        for word in words:
            if len(word) > len(char_to_digit):
                return False
            for c in word:
                if c not in char_to_digit:
                    return False
        for c in result:
            if c not in char_to_digit:
                return False
        for word in words:
            num = 0
            for c in word:
                num = num * 10 + char_to_digit[c]
            if num < 0:
                return False
        res_num = 0
        for c in result:
            res_num = res_num * 10 + char_to_digit[c]
        if res_num < 0:
            return False
        for word in words:
            num = 0
            for c in word:
                num = num * 10 + char_to_digit[c]
            if num < 0:
                return False
        return sum(num for word in words for num in [0] * len(word) for c in word for num in [0] * len(word)) == res_num

    if backtrack(0, set(), {}, unique_chars, words, result):
        print("true")
    else:
        print("false")

if __name__ == '__main__':
    solve()