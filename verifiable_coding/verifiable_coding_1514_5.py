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
        
        # Total difference in all elements
        total_diff = da + db + dc
        
        # The minimum cost is the absolute value of the total difference divided by 2
        # Because each merge/split operation can adjust the total difference by 2
        min_cost = abs(total_diff) // 2
        
        results.append(str(min_cost))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()