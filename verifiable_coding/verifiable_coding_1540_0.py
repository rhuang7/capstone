import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        N = int(data[index])
        index += 1
        K = int(data[index])
        index += 1
        
        if K >= N and K % N == 0:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()