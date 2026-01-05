import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        N = int(data[index])
        M = int(data[index + 1])
        index += 2
        
        if (N % 2 == 0 and M % 2 == 0) or (N % 2 == 1 and M % 2 == 1):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()