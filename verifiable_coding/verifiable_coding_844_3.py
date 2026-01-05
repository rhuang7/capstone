import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split(b'\n')
    idx = 0
    N, K = map(int, input[idx].split())
    idx += 1
    open_tweets = [0] * N
    for _ in range(K):
        line = input[idx].strip()
        idx += 1
        if line.startswith(b'CLICK'):
            parts = line.split()
            x = int(parts[1]) - 1
            open_tweets[x] = 1 - open_tweets[x]
        elif line == b'CLOSEALL':
            open_tweets = [0] * N
        print(sum(open_tweets))

if __name__ == '__main__':
    solve()