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
        
        # Bricks from top to bottom
        bricks = [W1, W2, W3]
        
        min_hits = 0
        
        while len(bricks) > 0:
            # Try both possible orders (original and reversed)
            # Try original order
            current = bricks
            total = 0
            k = 0
            for i in range(len(current)):
                total += current[i]
                if total > S:
                    break
                k += 1
            if k > 0:
                # Remove the first k bricks
                bricks = bricks[k:]
                min_hits += 1
                continue
            
            # Try reversed order
            current = bricks[::-1]
            total = 0
            k = 0
            for i in range(len(current)):
                total += current[i]
                if total > S:
                    break
                k += 1
            if k > 0:
                # Remove the first k bricks (which are the last k in original order)
                bricks = bricks[k:]
                min_hits += 1
                continue
        
        print(min_hits)

if __name__ == '__main__':
    solve()