import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    cases = data[1:]
    
    for i in range(t):
        n = int(cases[i*2])
        m = int(cases[i*2+1])
        if (n == 1 and m % 2 == 0) or (m == 1 and n % 2 == 0) or (n % 2 == 0 and m % 2 == 0):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()