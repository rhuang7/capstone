import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(T):
        M = int(data[index])
        N = int(data[index + 1])
        index += 2
        
        count_pairs = 0
        count_x = 0
        
        # For x in 1 to M
        for x in range(1, M + 1):
            # For y in 1 to N
            for y in range(1, N + 1):
                # Check if x*y + x + y equals the concatenation of x and y as strings
                if x * y + x + y == int(str(x) + str(y)):
                    count_pairs += 1
                    count_x += 1
        results.append(f"{count_pairs} {count_x}")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()