import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        W = list(map(int, data[idx:idx+N]))
        idx += N
        
        max_w = max(W)
        count = 0
        
        # Find all positions where the maximum occurs
        max_positions = [i for i, val in enumerate(W) if val == max_w]
        
        # For each possible shift k, check if the first half of the shifted array
        # does not contain any maximum value
        for k in range(N):
            # Shift the array by k
            shifted = W[k:] + W[:k]
            # Check first half
            valid = True
            for i in range(N//2):
                if shifted[i] == max_w:
                    valid = False
                    break
            if valid:
                count += 1
        
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()