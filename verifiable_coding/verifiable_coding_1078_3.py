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
        
        # Possible configurations (original and reversed)
        configs = [
            [W1, W2, W3],
            [W3, W2, W1]
        ]
        
        min_hits = float('inf')
        
        for config in configs:
            bricks = config
            hits = 0
            
            while bricks:
                # Try to take the top k bricks
                total = 0
                k = 0
                for i in range(len(bricks)):
                    total += bricks[i]
                    if total > S:
                        break
                    k += 1
                
                # If k is 0, then no bricks can be broken, but the problem states it's guaranteed to be possible
                # So we must have at least one brick that can be broken
                # So we take the first brick
                if k == 0:
                    k = 1
                
                # Remove the top k bricks
                bricks = bricks[k:]
                hits += 1
            
            min_hits = min(min_hits, hits)
        
        results.append(str(min_hits))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()