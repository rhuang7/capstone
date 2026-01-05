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
        min_num = N_str
        
        for i in range(n):
            # Try removing the i-th digit and appending d
            new_num = N_str[:i] + N_str[i+1:] + [d]
            # Convert to string and compare
            current = ''.join(new_num)
            if current < ''.join(min_num):
                min_num = new_num
        
        print(''.join(min_num))

if __name__ == '__main__':
    solve()