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
    output = []
    
    for _ in range(K):
        cmd = data[idx]
        idx += 1
        if cmd == 'CLICK':
            X = int(data[idx]) - 1
            idx += 1
            open_tweets[X] = 1 - open_tweets[X]
            output.append(str(sum(open_tweets)))
        elif cmd == 'CLOSEALL':
            open_tweets = [0] * N
            output.append('0')
    
    print('\n'.join(output))

if __name__ == '__main__':
    solve()