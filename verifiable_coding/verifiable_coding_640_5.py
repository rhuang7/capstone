import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    results = []
    for _ in range(T):
        X = int(data[idx])
        Y = int(data[idx+1])
        idx += 2
        if X == Y:
            results.append('0')
            continue
        power = 0
        while X != Y:
            if X > Y:
                power += X
                Y += X
            else:
                power += Y
                X += Y
        results.append(str(power))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()