import sys

def solve():
    S = sys.stdin.buffer.read().decode().strip()
    result = []
    vowels = "aeiouAEIOU"
    for char in S:
        if char in vowels:
            continue
        # Check if it's an uppercase consonant and convert to lowercase
        if char.isupper():
            result.append(f".{char.lower()}")
        else:
            result.append(f".{char}")
    print(''.join(result))

if __name__ == '__main__':
    solve()