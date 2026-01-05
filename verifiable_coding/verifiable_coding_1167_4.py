import sys

def solve():
    S = sys.stdin.buffer.read().decode().strip()
    result = []
    vowels = "aeiouAEIOU"
    for char in S:
        if char in vowels:
            continue
        # Convert to lowercase
        lower_char = char.lower()
        # Add '.' before the consonant
        result.append(f".{lower_char}")
    print(''.join(result))

if __name__ == '__main__':
    solve()