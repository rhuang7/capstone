import sys
import collections

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    h = list(map(int, data[1:]))
    
    # Count occurrences of each height
    count = collections.defaultdict(int)
    for height in h:
        count[height] += 1
    
    # For each segment, determine the range of heights and increment counts
    # We use a frequency array to track how many times each height is covered
    # Since heights can be up to 1e9, we use a dictionary to track the frequency
    freq = collections.defaultdict(int)
    
    for i in range(N - 1):
        a = h[i]
        b = h[i + 1]
        if a < b:
            # Increasing
            for height in range(a, b + 1):
                freq[height] += 1
        else:
            # Decreasing
            for height in range(b, a + 1):
                freq[height] += 1
    
    # Find the maximum frequency
    max_k = 0
    for k in freq.values():
        if k > max_k:
            max_k = k
    
    print(max_k)

if __name__ == '__main__':
    solve()