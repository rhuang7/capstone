import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(T):
        L1 = data[index]
        L2 = data[index+1]
        L3 = data[index+2]
        N = int(data[index+3])
        index += 4
        
        # Convert binary strings to actual binary string
        binary = L1 + L2 * N + L3
        
        # Convert binary to integer
        L = int(binary, 2)
        
        # Compute the number of accesses
        count = 0
        while L > 0:
            count += 1
            L = L & (L + 1)
        
        results.append(str(count))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()