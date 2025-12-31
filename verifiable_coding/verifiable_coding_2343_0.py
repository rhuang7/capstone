import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    idx = 1
    results = []
    for _ in range(t):
        d = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        # The number of valid arrays is equal to the sum of the first d numbers
        # modulo m, because each array corresponds to a unique number from 1 to d
        # and each number is a valid array of length 1
        res = sum(range(1, d+1)) % m
        results.append(res)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()