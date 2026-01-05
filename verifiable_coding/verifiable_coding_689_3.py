import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    records = data[1:]
    
    zebra_positions = set()
    spits = {}
    
    for i in range(t):
        a = int(records[2*i])
        b = int(records[2*i + 1])
        spits[i] = (a, b)
        zebra_positions.add(a)
    
    for i in range(t):
        a, b = spits[i]
        target = a + b
        if target in zebra_positions:
            for j in range(t):
                if i == j:
                    continue
                a_j, b_j = spits[j]
                if a_j == target and b_j == -(b):
                    print("YES")
                    return
    
    print("NO")

if __name__ == '__main__':
    solve()