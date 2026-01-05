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
    
    # Preprocess: for each value, store the count of unique even values up to that value
    prefix = [0] * (27)  # since values go from 1 to 26
    for i in range(1, 27):
        prefix[i] = prefix[i-1] + unique_even.get(i, 0)
    
    # Process queries
    for x, y in queries:
        res = prefix[y] - prefix[x-1]
        print(res)

if __name__ == '__main__':
    solve()