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
        
        # The total number of operations needed to balance the differences
        # using merge and split operations (cost 0)
        # The total number of operations that must be done with individual steps (cost 1)
        # is the sum of the absolute values of the differences, minus twice the minimum of the sum of the positive differences
        # because merge and split can balance the differences without cost
        total_diff = abs(da) + abs(db) + abs(dc)
        min_positive = min(abs(da), abs(db), abs(dc))
        min_total = total_diff - 2 * min_positive
        
        results.append(min_total)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()