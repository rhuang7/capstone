import sys

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        P1 = int(data[index])
        P2 = int(data[index+1])
        K = int(data[index+2])
        index += 3
        total = P1 + P2
        if total % K == 0:
            print("COOK")
        else:
            print("CHEF")

if __name__ == '__main__':
    solve()