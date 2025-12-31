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
        A = list(map(int, data[idx:idx+N]))
        idx += N
        total = 0
        for a in A:
            total += a
        speed = 1
        while True:
            current_time = 0
            for a in A:
                if current_time >= a * speed:
                    break
                current_time += a * speed
            else:
                results.append(str(speed))
                break
            speed += 1
    print('\n'.join(results))