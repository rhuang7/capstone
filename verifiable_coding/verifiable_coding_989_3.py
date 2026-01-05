import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        X = int(input[idx])
        Y = int(input[idx+1])
        K = int(input[idx+2])
        idx += 3
        total = X + Y
        serving = "Chef"
        for i in range(0, total, K):
            if serving == "Chef":
                serving = "Paja"
            else:
                serving = "Chef"
        print(serving)

if __name__ == '__main__':
    solve()