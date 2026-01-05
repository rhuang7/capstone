import sys

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        N = int(data[index])
        index += 1
        S = data[index]
        index += 1
        R = data[index]
        index += 1
        if sorted(S) != sorted(R):
            print("NO")
        else:
            print("YES")

if __name__ == '__main__':
    solve()