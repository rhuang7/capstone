import sys

def solve():
    import bisect
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
        # Find the transition point using bisect
        transition_point = bisect.bisect_right(arr, 0)
        print(transition_point)

if __name__ == '__main__':
    solve()