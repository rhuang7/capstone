import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    
    for K in cases:
        if K == 1:
            print("1")
        else:
            # First part: K rows of K 1's
            for _ in range(K):
                print("1" * K)
            # Second part: K-1 rows of alternating 1's and spaces
            for i in range(1, K):
                row = ""
                for j in range(K):
                    if j % 2 == 0:
                        row += "1"
                    else:
                        row += " "
                print(row)
                
if __name__ == '__main__':
    solve()