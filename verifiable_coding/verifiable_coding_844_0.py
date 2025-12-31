import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    idx = 0
    N = int(input[idx])
    idx += 1
    K = int(input[idx])
    idx += 1

    open_tweets = [0] * N
    for _ in range(K):
        cmd = input[idx]
        idx += 1
        if cmd == 'CLICK':
            X = int(input[idx]) - 1
            idx += 1
            open_tweets[X] = 1 - open_tweets[X]
        elif cmd == 'CLOSEALL':
            open_tweets = [0] * N
        print(sum(open_tweets))

if __name__ == '__main__':
    solve()