import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        N = data[index]
        d = int(data[index + 1])
        index += 2
        
        N_str = list(N)
        n = len(N_str)
        min_num = N_str.copy()
        
        for i in range(n):
            # Try removing each digit and appending d
            temp = N_str[:i] + N_str[i+1:] + [d]
            # Check if this is the smallest so far
            if temp < min_num:
                min_num = temp
        
        # Convert to string and print
        print(''.join(min_num))
        
if __name__ == '__main__':
    solve()