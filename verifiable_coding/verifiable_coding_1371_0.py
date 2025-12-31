import sys

def solve():
    input = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        N, K = int(input[idx]), int(input[idx+1])
        idx += 2
        arr = list(map(int, input[idx:idx+N]))
        idx += N
        count = 0
        for num in arr:
            if (num + K) % 7 == 0:
                count += 1
        print(count)

if __name__ == '__main__':
    solve()