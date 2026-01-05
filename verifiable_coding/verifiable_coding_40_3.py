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
        # This subsequence represents the elements that are already in the correct order
        # The minimum number of operations is the number of unique elements minus the length of this subsequence
        sorted_unique = sorted(unique)
        lcs = 0
        dp = [1] * m
        for i in range(m):
            for j in range(i):
                if sorted_unique[j] < sorted_unique[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        lcs = max(dp)
        results.append(m - lcs)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()