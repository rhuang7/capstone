import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    numbers = list(map(int, data[1:t+1]))
    numbers.sort()
    for num in numbers:
        print(num)

if __name__ == '__main__':
    solve()