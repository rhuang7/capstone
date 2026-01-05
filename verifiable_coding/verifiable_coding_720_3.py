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
        cnt_0 = 0
        cnt_1 = 0
        for j in range(n):
            if S[j] == '0':
                cnt_0 += 1
            else:
                cnt_1 += 1
            if cnt_0 == cnt_1 * cnt_1:
                beauty += 1
        results.append(beauty)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()