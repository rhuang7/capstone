import sys
import collections

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    q = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(q):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        # Count frequency of each number
        freq = collections.Counter(a)
        # Get sorted unique elements
        unique = sorted(freq.keys())
        m = len(unique)
        
        # If already sorted, answer is 0
        if a == sorted(a):
            results.append(0)
            continue
        
        # Find the longest increasing subsequence of unique elements in the sorted array
        # This subsequence represents elements that are already in the correct order and do not need to be moved
        # The minimum number of operations is m - length of this subsequence
        sorted_unique = sorted(unique)
        lcs = 0
        for num in a:
            if num in freq:
                lcs += 1
        # Actually, we need to find the longest increasing subsequence of unique elements in the sorted array
        # But since the unique elements are already sorted, the longest increasing subsequence is the entire list
        # So the minimum number of operations is m - 1
        results.append(m - 1)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()