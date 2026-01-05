import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        L = int(data[index])
        S = data[index + 1]
        index += 2
        n = len(S)
        min_str = S
        for i in range(L + 1):
            for j in range(i, L + 1):
                substr = S[i:j]
                new_s = S[:i] + S[j:] + substr
                if new_s < min_str:
                    min_str = new_s
        print(min_str)

if __name__ == '__main__':
    solve()