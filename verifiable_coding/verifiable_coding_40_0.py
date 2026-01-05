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
        
        # Find the longest consecutive increasing subsequence in the unique sorted list
        # This subsequence represents elements that are already in the correct order
        # The minimum number of operations is m - length of this subsequence
        max_len = 1
        current_len = 1
        for i in range(1, m):
            if unique[i] == unique[i - 1] + 1:
                current_len += 1
                max_len = max(max_len, current_len)
            else:
                current_len = 1
        
        results.append(m - max_len)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()