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
            # The selected position is the minimum in the current round
            # So the maximum value in the array is the distance from the selected position
            # We need to find the maximum value in the array and update it
            # But since we are processing rounds in order, we can just track the maximum
            # value and update the array accordingly
            max_val = 0
            for i in range(N):
                if i < pos:
                    res[i] = res[i] + 1
                else:
                    res[i] = res[i] + 1
            # Find the maximum value in the array
            max_val = max(res)
            # Update the array to have the maximum value at the selected position
            for i in range(N):
                if i < pos:
                    res[i] = max_val - (pos - i)
                else:
                    res[i] = max_val - (i - pos)
        # Append the result for this test case
        results.append(' '.join(map(str, res)))
    # Print all results
    print('\n'.join(results))

if __name__ == '__main__':
    solve()