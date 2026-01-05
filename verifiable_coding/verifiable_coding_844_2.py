import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    K = int(data[idx])
    idx += 1
    open_tweets = [0] * N
    for _ in range(K):
        cmd = data[idx]
        if cmd == 'CLICK':
            X = int(data[idx + 1]) - 1
            idx += 2
            open_tweets[X] = 1 - open_tweets[X]
        elif cmd == 'CLOSEALL':
            idx += 1
            open_tweets = [0] * N
        print(sum(open_tweets))

if __name__ == '__main__':
    solve()