import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    numbers = list(map(int, input[1:T+1]))
    for num in numbers:
        print(str(num).count('4'))

if __name__ == '__main__':
    solve()