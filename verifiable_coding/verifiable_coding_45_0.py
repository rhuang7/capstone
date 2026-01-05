import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    cases = list(map(int, data[1:t+1]))
    
    for x in cases:
        count = 0
        i = 1
        while True:
            total = i * (i + 1) // 2
            if total > x:
                break
            count += 1
            i += 1
        print(count)

if __name__ == '__main__':
    solve()