import sys

def solve():
    input = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        N = int(input[idx])
        idx += 1
        A = list(map(int, input[idx:idx+N]))
        idx += N
        if len(set(A)) == N:
            print("prekrasnyy")
        else:
            print("ne krasivo")

if __name__ == '__main__':
    solve()