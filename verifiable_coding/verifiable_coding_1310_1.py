import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]
    
    for case in cases:
        stamps = 0
        total_cost = 0
        for c in case:
            if c == 'M':
                total_cost += 3
                stamps += 1
            else:
                total_cost += 4
                stamps += 1
            while stamps >= 6:
                stamps -= 6
                total_cost += 3  # Free drink is not counted, so no addition
        print(total_cost)

if __name__ == '__main__':
    solve()