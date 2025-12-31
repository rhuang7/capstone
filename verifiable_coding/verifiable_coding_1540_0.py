import sys

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    idx = 1
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        K = int(data[idx])
        idx += 1
        
        if K >= N and K % N == 0:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()