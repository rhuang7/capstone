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
        M = int(data[idx+1])
        idx += 2
        positions = list(map(int, data[idx:idx+M]))
        idx += M
        # Initialize result array with 0s
        res = [0] * N
        # For each round, update the result array
        for pos in positions:
            # The selected position is the minimum value in the current array
            min_val = min(res)
            # Update the array based on the selected position
            for i in range(N):
                if i < pos:
                    res[i] = min_val + (pos - i)
                else:
                    res[i] = min_val + (i - pos)
        results.append(' '.join(map(str, res)))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()