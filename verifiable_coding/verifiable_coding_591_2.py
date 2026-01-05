import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    
    for N in cases:
        result = ""
        # Start from 1 and find the Nth number whose digits sum to a multiple of 10
        count = 0
        num = 1
        while True:
            s = sum(int(d) for d in str(num))
            if s % 10 == 0 and s > 0:
                count += 1
                if count == N:
                    result = str(num)
                    break
            num += 1
        print(result)
        
if __name__ == '__main__':
    solve()