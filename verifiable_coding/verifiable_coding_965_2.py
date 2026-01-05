import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        N = int(input[idx])
        K = int(input[idx+1])
        idx += 2
        if K == 0:
            print("0 0")
            continue
        if N < K:
            print(f"0 {N}")
        else:
            students = N // K
            teacher = N % K
            print(f"{students} {teacher}")

if __name__ == '__main__':
    solve()