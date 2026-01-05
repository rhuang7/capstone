import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    results = []
    for _ in range(T):
        a = int(data[idx])
        b = int(data[idx+1])
        c = int(data[idx+2])
        idx += 3
        # The largest number <= c that leaves remainder b when divided by a is:
        # If b <= c, then it's c - ((c - b) % a)
        # Otherwise, it's b - (a - (c - b) % a)
        # But since b < a and c > a, we can directly compute:
        remainder = (c - b) % a
        result = c - remainder
        results.append(str(result))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()