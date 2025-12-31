import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    
    for k in cases:
        if k == 1:
            print("*")
        else:
            for i in range(k):
                if i == 0 or i == k-1:
                    print("*" * k)
                else:
                    print("*" + " " * (k-2) + "*")
                    
if __name__ == '__main__':
    solve()