import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    
    for k in cases:
        row = []
        num = 1
        for i in range(k):
            row.append(str(num))
            num += 1
        print(''.join(row))
        
if __name__ == '__main__':
    solve()