import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        N = int(data[index])
        M = int(data[index+1])
        K = int(data[index+2])
        index += 3
        
        # Calculate the initial difference
        diff = abs(N - M)
        
        # Use the coins to reduce the difference
        # The maximum possible reduction is min(K, diff)
        max_reduct = min(K, diff)
        min_diff = diff - max_reduct
        
        print(min_diff)

if __name__ == '__main__':
    solve()