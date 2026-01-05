import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    S = data[0].decode()
    Q = int(data[1])
    queries = [(int(data[2 + 2*i]), int(data[2 + 2*i + 1])) for i in range(Q)]
    
    from collections import defaultdict

    # Preprocess: count frequency of each character in S
    freq = defaultdict(int)
    for c in S:
        freq[c] += 1

    # Preprocess: for each position, store the character and its value
    pos_char = []
    for i in range(len(S)):
        pos_char.append((i + 1, ord(S[i]) - ord('a') + 1))  # i+1 is 1-based position

    # Preprocess: for each value, store the positions where it occurs
    value_positions = defaultdict(list)
    for pos, val in pos_char:
        value_positions[val].append(pos)

    # Preprocess: for each value, store the sorted list of positions
    for val in value_positions:
        value_positions[val].sort()

    # Function to count unique even values in [X, Y]
    def count_unique_even(X, Y):
        count = 0
        for val in value_positions:
            if val % 2 == 0:
                positions = value_positions[val]
                # Binary search to find how many positions are in [X, Y]
                left = bisect.bisect_left(positions, X)
                right = bisect.bisect_right(positions, Y)
                count += right - left
        return count

    import bisect

    for X, Y in queries:
        print(count_unique_even(X, Y))

if __name__ == '__main__':
    solve()