import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    
    for k in cases:
        if k == 1:
            print("1")
        else:
            # First part: k lines of k 1's
            for _ in range(k):
                print("1" * k)
            # Second part: (k-1) lines of alternating 1's and spaces
            for i in range(1, k):
                line = ""
                for j in range(k):
                    if j % 2 == 0:
                        line += "1"
                    else:
                        line += " "
                print(line)
                
if __name__ == '__main__':
    solve()