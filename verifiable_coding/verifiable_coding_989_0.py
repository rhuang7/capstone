import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        X = int(data[index])
        Y = int(data[index+1])
        K = int(data[index+2])
        index += 3
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