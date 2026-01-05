import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]

    for case in cases:
        stamps = 0
        spent = 0
        for c in case:
            if c == 'M':
                spent += 3
                stamps += 1
            else:
                spent += 4
                stamps += 1
            while stamps >= 6:
                stamps -= 6
                spent -= 3  # free drink, no cost
        print(spent)

if __name__ == '__main__':
    solve()