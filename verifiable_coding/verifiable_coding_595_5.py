import sys

def solve():
    S = sys.stdin.buffer.read().decode().strip()
    n = len(S)
    total = 0

    # Precompute all palindromic substrings
    is_pal = [[False] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if i == j:
                is_pal[i][j] = True
            elif S[i] == S[j]:
                if j == i + 1:
                    is_pal[i][j] = True
                else:
                    is_pal[i][j] = is_pal[i + 1][j - 1]

    # Count valid pairs
    for i in range(n):
        for j in range(i + 1, n):
            if is_pal[i][j]:
                # s1 is from i to j, s2 starts after j
                for k in range(j + 1, n):
                    for l in range(k, n):
                        if is_pal[k][l]:
                            total += 1

    print(total)

if __name__ == '__main__':
    solve()