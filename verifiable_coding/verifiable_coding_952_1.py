import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for s in data:
        total = 0
        for c in s:
            if c not in vowels:
                total += abs(ord(c) - ord('a') - (ord(c) - ord('a') - 4))
        print(total)

if __name__ == '__main__':
    solve()