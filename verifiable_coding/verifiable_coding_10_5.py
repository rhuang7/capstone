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
        best_len = 0
        
        # Try all possible starting points
        for i in range(n):
            # Find the farthest element to the left
            left = pos[1]
            if left < i:
                left = pos[1]
            # Find the farthest element to the right
            right = pos[n]
            if right > i:
                right = pos[n]
            
            # Check the maximum sum for starting at i
            current_sum = 0
            current_seq = []
            # Try going left first
            current_seq.append(p[i])
            current_sum = 0
            for j in range(i-1, -1, -1):
                if abs(p[i] - p[j]) > current_sum:
                    current_sum += abs(p[i] - p[j])
                    current_seq.append(p[j])
                    if len(current_seq) > 2:
                        break
            # Try going right first
            if len(current_seq) < 2:
                current_seq = [p[i]]
                for j in range(i+1, n):
                    if abs(p[i] - p[j]) > current_sum:
                        current_sum += abs(p[i] - p[j])
                        current_seq.append(p[j])
                        if len(current_seq) > 2:
                            break
            
            if current_sum > max_sum or (current_sum == max_sum and len(current_seq) < best_len):
                max_sum = current_sum
                best_seq = current_seq
                best_len = len(current_seq)
        
        results.append(str(len(best_seq)))
        results.append(' '.join(map(str, best_seq)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()