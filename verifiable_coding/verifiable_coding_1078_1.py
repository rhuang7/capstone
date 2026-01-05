import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
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
            # Check if current order is better
            min_hits = float('inf')
            
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
                min_hits = 1 + min_hits
            
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
                min_hits = 1 + min_hits
            
            # Choose the order with minimum hits
            if min_hits == float('inf'):
                # This should not happen as per problem statement
                min_hits = 1
            
            hits += min_hits
            
            # Update bricks after hitting
            # Remove the top k bricks
            bricks = bricks[k:]
        
        results.append(str(hits))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()