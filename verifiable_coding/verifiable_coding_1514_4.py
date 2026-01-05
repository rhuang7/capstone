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
        
        # Compute the differences
        da = a0 - x
        db = b0 - y
        dc = c0 - z
        
        # The total difference in the sum of the tuple
        sum_diff = (a0 + b0 + c0) - (x + y + z)
        
        # If the sum difference is not zero, we need to perform operations to balance it
        # The operations that don't cost anything (merge and split) can only change the tuple in a way that keeps the sum the same
        # So if the sum difference is not zero, we need to perform some operations that cost 1 each
        
        # The minimum cost is the absolute value of the sum difference divided by 2
        # Because each operation that changes the sum by 2 (like adding 1 to one and subtracting 1 from another) costs 0
        # But if the sum difference is odd, we need one operation that costs 1 to adjust it
        # So the minimum cost is (abs(sum_diff) + 1) // 2
        
        cost = abs(sum_diff) // 2
        
        results.append(str(cost))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()