import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        score_dict = {}
        for _ in range(N):
            p = int(data[idx])
            s = int(data[idx + 1])
            idx += 2
            if 1 <= p <= 8:
                if p in score_dict:
                    if s > score_dict[p]:
                        score_dict[p] = s
                else:
                    score_dict[p] = s
        total = sum(score_dict.values())
        print(total)

if __name__ == '__main__':
    solve()