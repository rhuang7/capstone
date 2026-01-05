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
        
        # Find the longest consecutive increasing subsequence in the sorted unique list
        # that appears in the same order in the original array
        max_len = 1
        current_len = 1
        for i in range(1, m):
            # Check if the current unique element appears after the previous one in the original array
            prev = unique[i - 1]
            curr = unique[i]
            # Find the first occurrence of curr after the last occurrence of prev
            prev_pos = -1
            curr_pos = -1
            for j in range(len(a)):
                if a[j] == prev and prev_pos == -1:
                    prev_pos = j
                if a[j] == curr and curr_pos == -1:
                    curr_pos = j
            if curr_pos > prev_pos:
                current_len += 1
                max_len = max(max_len, current_len)
            else:
                current_len = 1
        
        # The minimum number of operations is the number of unique elements minus the length of the longest consecutive increasing subsequence
        results.append(m - max_len)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()