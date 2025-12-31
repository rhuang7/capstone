import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    a = list(map(int, data[1:]))
    
    from collections import Counter
    count = Counter(a)
    
    days = 0
    for c in count.values():
        if c > 2:
            days += c // 2 + (1 if c % 2 else 0)
        else:
            days += 1
    print(days)

if __name__ == '__main__':
    solve()