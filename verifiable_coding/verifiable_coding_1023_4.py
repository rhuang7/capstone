import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    
    for K in cases:
        row = 1
        current = 1
        for i in range(K):
            line = ""
            for j in range(row):
                line += str(current) + " "
                current += 1
            print(line.strip())
            row += 1

if __name__ == '__main__':
    solve()