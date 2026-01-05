import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    for i in range(1, T + 1):
        S = input[i]
        if len(S) < 2:
            print("NO")
            continue
        first = S[0]
        second = S[1]
        if first == second:
            print("NO")
            continue
        is_alternating = True
        for j in range(2, len(S)):
            if (j % 2 == 0 and S[j] != first) or (j % 2 == 1 and S[j] != second):
                is_alternating = False
                break
        print("YES" if is_alternating else "NO")

if __name__ == '__main__':
    solve()