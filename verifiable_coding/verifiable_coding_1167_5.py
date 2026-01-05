import sys

def solve():
    S = sys.stdin.buffer.read().decode().strip()
    result = []
    vowels = "aeiouAEIOU"
    for char in S:
        if char in vowels:
            continue
        # Check if it's an uppercase consonant
        if char.isupper():
            result.append('.' + char.lower())
        else:
            result.append('.' + char)
    print(''.join(result))

if __name__ == '__main__':
    solve()