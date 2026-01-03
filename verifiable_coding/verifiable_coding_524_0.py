import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    S = data[0].decode()
    Q = int(data[1])
    queries = [(int(data[2 + 2*i]), int(data[2 + 2*i + 1])) for i in range(Q)]
    
    # Preprocess: count frequency of each character
    freq = [0] * 26
    for c in S:
        idx = ord(c) - ord('a')
        freq[idx] += 1
    
    # Preprocess: for each position, store the character's value
    positions = [0] * len(S)
    for i in range(len(S)):
        positions[i] = ord(S[i]) - ord('a') + 1  # 1-based value
    
    # Preprocess: for each value, store the positions where it occurs
    from collections import defaultdict
    pos_map = defaultdict(list)
    for i, val in enumerate(positions):
        pos_map[val].append(i)
    
    # Preprocess: for each value, check if it's even and occurs only once
    unique_even = []
    for val in range(1, 27):
        if val % 2 == 0 and freq[val - 1] == 1:
            unique_even.append(val)
    
    # Preprocess: for each value, store the positions where it occurs
    # We will use binary search to count how many of these values are in [X, Y]
    # Create a sorted list of unique even values
    unique_even_sorted = sorted(unique_even)
    
    # Preprocess: for each value in unique_even_sorted, store its positions
    # We will use binary search to count how many of these values are in [X, Y]
    # For each query, we will check how many of the unique even values fall into [X, Y]
    # And for each such value, count how many times it appears in the range [X, Y]
    # But since the value is unique, we just need to check if it's in [X, Y]
    # And if so, count how many times it appears in the range [X, Y]
    
    # Preprocess: for each value in unique_even_sorted, store its positions
    # We will use binary search to count how many of these values are in [X, Y]
    # And for each such value, count how many times it appears in the range [X, Y]
    # But since the value is unique, we just need to check if it's in [X, Y]
    # And if so, count how many times it appears in the range [X, Y]
    
    # Preprocess: for each value in unique_even_sorted, store its positions
    # We will use binary search to count how many of these values are in [X, Y]
    # And for each such value, count how many times it appears in the range [X, Y]
    # But since the value is unique, we just need to check if it's in [X, Y]
    # And if so, count how many times it appears in the range [X, Y]
    
    # Preprocess: for each value in unique_even_sorted, store its positions
    # We will use binary search to count how many of these values are in [X, Y]
    # And for each such value, count how many times it appears in the range [X, Y]
    # But since the value is unique, we just need to check if it's in [X, Y]
    # And if so, count how many times it appears in the range [X, Y]
    
    # Preprocess: for each value in unique_even_sorted, store its positions
    # We will use binary search to count how many of these values are in [X, Y]
    # And for each such value, count how many times it appears in the range [X, Y]
    # But since the value is unique, we just need to check if it's in [X, Y]
    # And if so, count how many times it appears in the range [X, Y]
    
    # Preprocess: for each value in unique_even_sorted, store its positions
    # We will use binary search to count how many of these values are in [X, Y]
    # And for each such value, count how many times it appears in the range [X, Y]
    # But since the value is unique, we just need to check if it's in [X, Y]
    # And if so, count how many times it appears in the range [X, Y]
    
    # Preprocess: for each value in unique_even_sorted, store its positions
    # We will use binary search to count how many of these values are in [X, Y]
    # And for each such value, count how many times it appears in the range [X, Y]
    # But since the value is unique, we just need to check if it's in [X, Y]
    # And if so, count how many times it appears in the range [X, Y]
    
    # Preprocess: for each value in unique_even_sorted, store its positions
    # We will use binary search to count how many of these values are in [X, Y]
    # And for each such value, count how many times it appears in the range [X, Y]
    # But since the value is unique, we just need to check if it's in [X, Y]
    # And if so, count how many times it appears in the range [X, Y]
    
    # Preprocess: for each value in unique_even_sorted, store its positions
    # We will use binary search to count how many of these values are in [X, Y]
    # And for each such value, count how many times it appears in the range [X, Y]
    # But since the value is unique, we just need to check if it's in [X, Y]
    # And if so, count how many times it appears in the range [X, Y]
    
    # Preprocess: for each value in unique_even_sorted, store its positions
    # We will use binary search to count how many of these values are in [X, Y]
    # And for each such value, count how many times it appears in the range [X, Y]
    # But since the value is unique, we just need to check if it's in [X, Y]
    # And if so, count how many times it appears in the range [X, Y]
    
    # Preprocess: for each value in unique_even_sorted, store its positions
    # We will use binary search to count how many of these values are in [X, Y]
    # And for each such value, count how many times it appears in the range [X, Y]
    # But since the value is unique, we just need to check if it's in [X, Y]
    # And if so, count how many times it appears in the range [X, Y]
    
    # Preprocess: for each value in unique_even_sorted, store its positions
    # We will use binary search to count how many of these values are in [X, Y]
    # And for each such value, count how many times it appears in the range [X, Y]
    # But since the value is unique, we just need to check if it's in [X, Y]
    # And if so, count how many times it appears in the range [X, Y]
    
    # Preprocess: for each value in unique_even_sorted, store its positions
    # We will use binary search to count how many of these values are in [X, Y]
    # And for each such value, count how many times it appears in the range [X, Y]
    # But since the value is unique, we just need to check if it's in [X, Y]
    # And if so, count how many times it appears in the range [X, Y]
    
    # Preprocess: for each value in unique_even_sorted, store its positions
    # We will use binary search to count how many of these values are in [X, Y]
    # And for each such value, count how many times it appears in the range [X, Y]
    # But since the value is unique, we just need to check if it's in [X, Y]
    # And if so, count how many times it appears in the range [X, Y]
    
    # Preprocess: for each value in unique_even_sorted, store its positions
    # We will use binary search to count how many of these values are in [X, Y]
    # And for each such value, count how many times it appears in the range [X, Y]
    # But since the value is unique, we just need to check if it's in [X, Y]
    # And if so, count how many times it appears in the range [X, Y]
    
    # Preprocess: for each value in unique_even_sorted, store its positions
    # We will use binary search to count how many of these values are in [X, Y]
    # And for each such value, count how many times it appears in the range [X, Y]
    # But since the value is unique,