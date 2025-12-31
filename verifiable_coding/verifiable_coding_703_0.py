import sys

def is_beautiful(n):
    while n > 0:
        if n & 1:
            if (n >> 1) & 1:
                return False
        n >>= 1
    return True

def find_previous_beautiful(n):
    while True:
        if is_beautiful(n):
            return n
        n -= 1

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        K = int(data[i])
        if is_beautiful(K):
            results.append(str(K))
        else:
            results.append(str(find_previous_beautiful(K)))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()