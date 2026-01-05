import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        C = list(map(int, data[idx:idx+N]))
        idx += N
        possible = True
        for i in range(N):
            if i + 2 >= N:
                possible = False
                break
            if C[i] != C[i+1] or C[i] != C[i+2]:
                possible = False
                break
        results.append("Yes" if possible else "No")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()