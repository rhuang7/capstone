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
        
        # For each valid k, check if the first half of the shifted array contains no max_w
        for k in range(N):
            # Shift by k, the first half is from position k to k + N//2 - 1
            # But since it's a circular array, we need to wrap around
            start = k
            end = k + N//2
            # Check if any of the elements in the first half is max_w
            valid = True
            for i in range(N//2):
                pos = (start + i) % N
                if W[pos] == max_w:
                    valid = False
                    break
            if valid:
                count += 1
        
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()