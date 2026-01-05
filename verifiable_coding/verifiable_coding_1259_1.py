import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        L = int(input[idx])
        R = int(input[idx+1])
        idx += 2
        count = 0
        for num in range(L, R + 1):
            if num % 10 in {2, 3, 9}:
                count += 1
        print(count)

if __name__ == '__main__':
    solve()