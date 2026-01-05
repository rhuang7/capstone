import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    
    for N in cases:
        result = ""
        digits = len(str(N))
        for i in range(1, digits + 1):
            result += str(i)
        print(result)
        
if __name__ == '__main__':
    solve()