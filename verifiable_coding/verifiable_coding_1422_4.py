import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        N = int(input[idx])
        idx += 1
        S = input[idx]
        idx += 1
        destroyed = [False] * N
        for i in range(N):
            if S[i] == '1':
                for j in range(max(0, i-1), min(N, i+2)):
                    destroyed[j] = True
        count = 0
        for i in range(N):
            if not destroyed[i]:
                count += 1
        print(count)

if __name__ == '__main__':
    solve()