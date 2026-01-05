import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    while True:
        n = int(data[idx])
        idx += 1
        if n == 0:
            break
        perm = list(map(int, data[idx:idx + n]))
        idx += n
        is_ambiguous = True
        inv = [0] * (n + 1)
        for i in range(n):
            inv[perm[i]] = i + 1
        for i in range(1, n + 1):
            if perm[i - 1] != inv[i]:
                is_ambiguous = False
                break
        if is_ambiguous:
            print("ambiguous")
        else:
            print("not ambiguous")

if __name__ == '__main__':
    solve()