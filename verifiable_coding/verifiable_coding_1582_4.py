import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    n = int(input[0])
    s = input[1] if len(input) > 1 else ""
    if n <= 1:
        print(0)
        return
    count = 0
    for i in range(1, n):
        if s[i] == s[i-1]:
            count += 1
    print(count)

if __name__ == '__main__':
    solve()