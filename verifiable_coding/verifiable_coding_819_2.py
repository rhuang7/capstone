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
        # Because the operation allows us to reduce the problem to gcd(x-1, y-1)
        # If gcd(x-1, y-1) is 1, then it is possible to reach the desired state
        if (x - 1) * (y - 1) == 0:
            print("YES")
        else:
            if sys.version_info[0] < 3:
                from math import gcd
            else:
                from math import gcd
            if gcd(x - 1, y - 1) == 1:
                print("YES")
            else:
                print("NO")

if __name__ == '__main__':
    solve()