import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        x = int(data[index])
        y = int(data[index + 1])
        index += 2
        
        # The problem reduces to checking if x and y are coprime
        # Because the operations allow us to reduce the problem to checking if gcd(x, y) == 1
        if x == 1 or y == 1:
            print("YES")
        else:
            if (x - 1) * (y - 1) % (x + y - 2) == 0:
                print("YES")
            else:
                print("NO")

if __name__ == '__main__':
    solve()