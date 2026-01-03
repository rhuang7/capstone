import sys

def solve():
    import sys
    from collections import Counter

    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    a = list(map(int, data[1:]))
    
    count = Counter(a)
    max_count = max(count.values())
    
    if max_count > 2:
        print(max_count)
    else:
        print(2)

if __name__ == '__main__':
    solve()