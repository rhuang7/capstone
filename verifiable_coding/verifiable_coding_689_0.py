import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    records = data[1:]
    
    zebras = set()
    for i in range(t):
        a = int(records[2*i])
        b = int(records[2*i + 1])
        target = a + b
        if target in zebras:
            print("YES")
            return
        zebras.add(a)
    
    print("NO")

if __name__ == '__main__':
    solve()