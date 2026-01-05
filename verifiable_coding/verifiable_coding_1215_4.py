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

    # Map unique characters to digits
    for i, c in enumerate(unique_chars):
        char_to_digit[c] = str(i)

    # Build equations
    equations = []
    for word in words:
        equations.append(''.join(char_to_digit[c] for c in word))
    equations.append(''.join(char_to_digit[c] for c in result))

    # Check if result is correct
    try:
        total = sum(int(e) for e in equations[:-1])
        if int(equations[-1]) == total:
            print("true")
        else:
            print("false")
    except:
        print("false")

if __name__ == '__main__':
    solve()