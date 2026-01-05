import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    scores = data[1:]
    p1 = 0
    p2 = 0
    max_lead = 0
    winner = 1
    for i in range(N):
        s = int(scores[2*i])
        t = int(scores[2*i + 1])
        p1 += s
        p2 += t
        lead = abs(p1 - p2)
        if lead > max_lead:
            max_lead = lead
            if p1 > p2:
                winner = 1
            else:
                winner = 2
    print(winner, max_lead)

if __name__ == '__main__':
    solve()