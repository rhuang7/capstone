import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    
    for _ in range(t):
        n = int(data[index])
        m = int(data[index+1])
        index += 2
        
        if (n == 1 and m % 2 == 1) or (m == 1 and n % 2 == 1):
            print("YES")
        elif (n % 2 == 0 and m % 2 == 0) or (n % 2 == 1 and m % 2 == 1):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()