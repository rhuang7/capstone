import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    
    for K in cases:
        if K == 1:
            print("1")
        else:
            # First part: K lines of K '1's
            for _ in range(K):
                print("1" * K)
            # Second part: K-1 lines of patterns
            for i in range(1, K):
                line = ""
                for j in range(i):
                    line += "1" + " " * (2*(i-j-1)) + "1"
                print(line)
                
if __name__ == '__main__':
    solve()