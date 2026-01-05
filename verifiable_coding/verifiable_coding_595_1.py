import sys

def solve():
    import sys
    S = sys.stdin.buffer.read().decode().strip()
    n = len(S)
    total = 0

    for i in range(n):
        for j in range(i + 1, n):
            s1 = S[i:j]
            s2 = S[j:]
            if (s1 + s2) == (s1 + s2)[::-1]:
                total += 1

    print(total)

if __name__ == '__main__':
    solve()