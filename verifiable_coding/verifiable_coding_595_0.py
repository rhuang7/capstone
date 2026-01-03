import sys

def solve():
    import sys
    S = sys.stdin.buffer.read().decode().strip()
    n = len(S)
    total = 0

    # Precompute palindrome check for all substrings
    is_pal = [[False] * n for _ in range(n)]
    for i in range(n):
        is_pal[i][i] = True
        if i < n - 1:
            is_pal[i][i + 1] = (S[i] == S[i + 1])
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            is_pal[i][j] = (S[i] == S[j]) and is_pal[i + 1][j - 1]

    # Iterate over all possible positions for s1 and s2
    for i in range(n):
        for j in range(i + 1, n):
            # Check if s1 = S[i..j-1] is a palindrome
            if is_pal[i][j - 1]:
                # Check all possible s2 starting after j
                for k in range(j, n):
                    for l in range(k, n):
                        if is_pal[k][l]:
                            total += 1

    print(total)

if __name__ == '__main__':
    solve()