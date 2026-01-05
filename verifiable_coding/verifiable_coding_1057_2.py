import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]

    def next_magical(n):
        n = int(n)
        while True:
            n += 1
            s = str(n)
            if all(c in {'4', '7'} for c in s):
                return n

    for n in cases:
        print(next_magical(n))

if __name__ == '__main__':
    solve()