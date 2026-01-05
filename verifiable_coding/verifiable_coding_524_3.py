import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    S = data[0].decode()
    Q = int(data[1])
    queries = [(int(data[2 + 2*i]), int(data[2 + 2*i + 1])) for i in range(Q)]
    
    # Preprocess: count frequency of each character
    freq = {}
    for c in S:
        val = ord(c) - ord('a') + 1
        if val in freq:
            freq[val] += 1
        else:
            freq[val] = 1
    
    # Preprocess: for each value, check if it's even and unique
    unique_even = {}
    for val in freq:
        if val % 2 == 0:
            unique_even[val] = 1
    
    # For each query, count how many unique even values fall in [X, Y]
    for X, Y in queries:
        count = 0
        for val in unique_even:
            if X <= val <= Y:
                count += 1
        print(count)

if __name__ == '__main__':
    solve()