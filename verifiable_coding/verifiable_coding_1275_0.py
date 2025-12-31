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
        # Initialize result array
        res = [0] * N
        # For each round
        for pos in positions:
            # Update the result array based on the selected position
            # The selected position is 0, and the numbers increase as we move left and right
            # So the maximum value for each position is the maximum distance from the selected position
            # So for each position i, the value is max(abs(i - pos), abs(i - pos))
            # But since the value increases as we move away from the selected position, the maximum value for each position is the maximum distance from the selected position
            # So for each position i, the value is max(abs(i - pos), abs(i - pos))
            # Wait, the value is the maximum distance from the selected position
            # So for each position i, the value is max(abs(i - pos), abs(i - pos))
            # But that's the same as abs(i - pos)
            # Wait, no. The value is the maximum number assigned during the rounds. So for each round, the value is the distance from the selected position. So for each position i, the value is the maximum distance from the selected position over all rounds.
            # So for each position i, the value is the maximum of abs(i - pos) over all rounds.
            # So for each round, we calculate the distance from the selected position and keep the maximum for each position.
            # So for each position i, res[i] = max(res[i], abs(i - pos))
            for i in range(N):
                res[i] = max(res[i], abs(i - pos))
        results.append(' '.join(map(str, res)))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()