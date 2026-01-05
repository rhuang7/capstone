import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    
    for p in cases:
        count = 0
        i = 11
        while p > 0:
            if p >= (1 << i):
                count += 1
                p -= (1 << i)
            i -= 1
        print(count)

if __name__ == '__main__':
    solve()