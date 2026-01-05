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
        N = int(data[index])
        L = int(data[index+1])
        R = int(data[index+2])
        index += 3
        
        # Minimum sum: all elements are 1
        min_sum = N * 1
        
        # Maximum sum: use the largest possible unique numbers such that each number is even and half is present
        # Start from 1 and double each time
        max_sum = 0
        current = 1
        count = 0
        
        while count < R and current <= 1 << 20:  # 1 << 20 is 1048576, which is larger than needed
            max_sum += current
            current <<= 1
            count += 1
        
        results.append(f"{min_sum} {max_sum}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()