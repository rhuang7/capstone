import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    
    for k in cases:
        pattern = ""
        num = 1
        for i in range(k):
            pattern += str(num)
            num += 1
        print(pattern)
        
if __name__ == '__main__':
    solve()