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
        speeds = list(map(int, data[idx:idx+N]))
        idx += N
        count = 0
        max_speed = -1
        for speed in reversed(speeds):
            if speed > max_speed:
                count += 1
                max_speed = speed
        results.append(str(count))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()