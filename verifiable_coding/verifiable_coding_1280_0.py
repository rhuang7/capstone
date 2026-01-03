import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        S = data[i]
        n = len(S)
        operations = 0
        for j in range(n // 2):
            left = S[j]
            right = S[n - 1 - j]
            if left < right:
                operations += (right - left)
            elif right < left:
                operations += (left - right)
        results.append(str(operations))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()