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
    char_values = [ord(c) - ord('a') + 1 for c in S]

    # Preprocess: for each value, store the positions where it occurs
    pos_map = defaultdict(list)
    for i, val in enumerate(char_values):
        pos_map[val].append(i + 1)  # 1-based index

    # Preprocess: for each value, check if it's even and unique
    unique_even_values = []
    for val in freq:
        if val % 2 == 0:
            unique_even_values.append(val)

    # For each query, count the number of positions in [X, Y] that have a value in unique_even_values
    for X, Y in queries:
        count = 0
        for val in unique_even_values:
            if val in pos_map:
                # Binary search for the first position >= X and <= Y
                positions = pos_map[val]
                left = 0
                right = len(positions) - 1
                res = -1
                while left <= right:
                    mid = (left + right) // 2
                    if positions[mid] >= X:
                        res = mid
                        right = mid - 1
                    else:
                        left = mid + 1
                if res != -1 and positions[res] <= Y:
                    count += 1
        print(count)

if __name__ == '__main__':
    solve()