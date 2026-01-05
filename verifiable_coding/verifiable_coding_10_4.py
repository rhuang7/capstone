import sys
import bisect

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        p = list(map(int, data[idx:idx+n]))
        idx += n
        
        # Create a position map for quick lookup
        pos = [0] * (n + 1)
        for i in range(n):
            pos[p[i]] = i
        
        # Find the maximum possible sum
        max_sum = 0
        best_seq = []
        
        # Try all possible pairs
        for i in range(n):
            for j in range(i + 1, n):
                current_sum = abs(p[i] - p[j])
                if current_sum > max_sum:
                    max_sum = current_sum
                    best_seq = [p[i], p[j]]
                elif current_sum == max_sum:
                    # Check if the current sequence is shorter
                    if len(best_seq) > 2:
                        best_seq = [p[i], p[j]]
        
        # If the best sequence is of length 2, we are done
        if len(best_seq) == 2:
            results.append(str(2))
            results.append(' '.join(map(str, best_seq)))
            continue
        
        # Otherwise, find the longest possible subsequence with max sum
        # We will use a greedy approach to build the sequence
        # We will try to find the maximum sum by extending the sequence
        
        # Initialize the best sequence
        best_seq = []
        max_sum = 0
        
        # Try all possible starting points
        for i in range(n):
            # Start with the current element
            current_seq = [p[i]]
            current_sum = 0
            # Try to extend the sequence to the right
            for j in range(i + 1, n):
                current_sum += abs(p[j] - p[j - 1])
                current_seq.append(p[j])
                if current_sum > max_sum:
                    max_sum = current_sum
                    best_seq = current_seq
                elif current_sum == max_sum:
                    # Check if the current sequence is shorter
                    if len(best_seq) > len(current_seq):
                        best_seq = current_seq
            # Try to extend the sequence to the left
            for j in range(i - 1, -1, -1):
                current_sum += abs(p[j] - p[j + 1])
                current_seq.insert(0, p[j])
                if current_sum > max_sum:
                    max_sum = current_sum
                    best_seq = current_seq
                elif current_sum == max_sum:
                    # Check if the current sequence is shorter
                    if len(best_seq) > len(current_seq):
                        best_seq = current_seq
        
        results.append(str(len(best_seq)))
        results.append(' '.join(map(str, best_seq)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()