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
        
        diff = abs(N - M)
        if K >= diff:
            print(0)
        else:
            print(diff)
            
if __name__ == '__main__':
    solve()