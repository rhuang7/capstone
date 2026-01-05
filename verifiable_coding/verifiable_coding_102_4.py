import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    cases = list(map(int, data[1:t+1]))
    
    for n in cases:
        count = 0
        for d in range(1, 10):
            num = 0
            for i in range(1, 10):
                num = num * 10 + d
                if num > n:
                    break
                count += 1
        print(count)

if __name__ == '__main__':
    solve()