import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        S = int(data[index])
        W1 = int(data[index+1])
        W2 = int(data[index+2])
        W3 = int(data[index+3])
        index += 4
        
        # Bricks are initially [W1, W2, W3]
        bricks = [W1, W2, W3]
        hits = 0
        
        while len(bricks) > 0:
            # Try both possible orders (original and reversed)
            min_hits = float('inf')
            
            # Option 1: do not reverse
            current = bricks
            total = 0
            k = 0
            while k < len(current) and total + current[k] <= S:
                total += current[k]
                k += 1
            if k > 0:
                min_hits = min(min_hits, k)
                bricks = current[k:]
            
            # Option 2: reverse
            current = bricks[::-1]
            total = 0
            k = 0
            while k < len(current) and total + current[k] <= S:
                total += current[k]
                k += 1
            if k > 0:
                min_hits = min(min_hits, k)
                bricks = current[k:]
            
            hits += min_hits
            bricks = bricks[min_hits:]
        
        print(hits)

if __name__ == '__main__':
    solve()