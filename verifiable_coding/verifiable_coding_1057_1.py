import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]

    def next_magical(n_str):
        n = int(n_str)
        while True:
            n += 1
            s = str(n)
            if all(c in {'4', '7'} for c in s):
                return s

    for case in cases:
        print(next_magical(case))

if __name__ == '__main__':
    solve()