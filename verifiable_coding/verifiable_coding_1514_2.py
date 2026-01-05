import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(T):
        a0 = int(data[index])
        b0 = int(data[index+1])
        c0 = int(data[index+2])
        x = int(data[index+3])
        y = int(data[index+4])
        z = int(data[index+5])
        index += 6
        
        # Compute the difference in each coordinate
        da = a0 - x
        db = b0 - y
        dc = c0 - z
        
        # The total number of operations needed is the sum of positive differences
        # because we can use merge and split operations to transfer values between coordinates
        # without cost
        total = 0
        if da > 0:
            total += da
        if db > 0:
            total += db
        if dc > 0:
            total += dc
        
        # The minimum cost is the sum of the positive differences
        results.append(str(total))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()