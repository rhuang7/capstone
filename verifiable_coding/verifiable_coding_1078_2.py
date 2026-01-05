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
            # Try both orientations
            # Option 1: no reversal
            total = 0
            k = 0
            for i in range(len(bricks)):
                total += bricks[i]
                if total > S:
                    break
                k += 1
            if k > 0:
                # Remove top k bricks
                bricks = bricks[k:]
                hits += 1
                continue
            
            # Option 2: reverse the bricks
            bricks = bricks[::-1]
            total = 0
            k = 0
            for i in range(len(bricks)):
                total += bricks[i]
                if total > S:
                    break
                k += 1
            if k > 0:
                # Remove top k bricks
                bricks = bricks[k:]
                hits += 1
                continue
        
        results.append(str(hits))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()