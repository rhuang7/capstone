import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]

    def is_magical(n):
        for ch in n:
            if ch not in {'4', '7'}:
                return False
        return True

    def next_magical(n):
        n = int(n)
        while True:
            n += 1
            if is_magical(str(n)):
                return n

    for case in cases:
        print(next_magical(case))

if __name__ == '__main__':
    solve()