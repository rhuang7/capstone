import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        arr = list(map(int, data[idx:idx+N]))
        idx += N
        inv_count = 0
        for i in range(N):
            for j in range(i+1, N):
                if arr[i] > arr[j]:
                    inv_count += 1
        print(inv_count)

if __name__ == '__main__':
    solve()