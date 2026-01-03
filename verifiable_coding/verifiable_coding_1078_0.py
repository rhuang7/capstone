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
            # Try original order
            total = 0
            k = 0
            for i in range(len(bricks)):
                total += bricks[i]
                if total > S:
                    break
                k += 1
            if k >= len(bricks):
                # All bricks can be broken in one hit
                hits += 1
                break
            # Try reversed order
            total_rev = 0
            k_rev = 0
            for i in range(len(bricks)):
                total_rev += bricks[-i-1]
                if total_rev > S:
                    break
                k_rev += 1
            if k_rev >= len(bricks):
                # All bricks can be broken in one hit if reversed
                hits += 1
                break
            
            # Choose the order that allows more bricks to be broken in one hit
            if k >= k_rev:
                # Use original order
                bricks = bricks[k:]
            else:
                # Reverse and use
                bricks = bricks[::-1]
                bricks = bricks[k_rev:]
            hits += 1
        
        results.append(str(hits))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()