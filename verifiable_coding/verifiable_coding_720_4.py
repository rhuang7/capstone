import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        S = data[i]
        beauty = 0
        n = len(S)
        for i in range(n):
            cnt0 = 0
            cnt1 = 0
            for j in range(i, n):
                if S[j] == '0':
                    cnt0 += 1
                else:
                    cnt1 += 1
                if cnt0 == cnt1 * cnt1:
                    beauty += 1
        results.append(beauty)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()