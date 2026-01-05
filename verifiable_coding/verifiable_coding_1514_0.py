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
        
        # Calculate the differences
        da = a0 - x
        db = b0 - y
        dc = c0 - z
        
        # The sum of the differences must be zero for the transformation to be possible
        # Since the problem says it is always possible, we don't need to check this
        
        # The minimum cost is the sum of the absolute values of the differences divided by 2
        # Because each merge/split operation can adjust two values at once
        cost = abs(da) + abs(db) + abs(dc)
        cost //= 2
        
        results.append(str(cost))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()