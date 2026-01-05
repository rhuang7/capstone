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
        
        N_str = str(N)
        min_num = N_str
        
        for i in range(len(N_str)):
            # Try removing the i-th digit and appending d
            new_num = N_str[:i] + N_str[i+1:] + str(d)
            if new_num < min_num:
                min_num = new_num
        
        print(min_num)

if __name__ == '__main__':
    solve()