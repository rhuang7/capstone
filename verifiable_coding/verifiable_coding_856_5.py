import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split(b'\n')
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        while idx < len(data) and data[idx].strip() == b'':
            idx += 1
        if idx >= len(data):
            break
        N = int(data[idx])
        idx += 1
        count = {}
        for _ in range(N):
            while idx < len(data) and data[idx].strip() == b'':
                idx += 1
            if idx >= len(data):
                break
            line = data[idx].strip().split()
            idx += 1
            w = line[0]
            s = int(line[1])
            if w in count:
                if count[w] == s:
                    count[w] += 1
                else:
                    pass
            else:
                count[w] = s
        results.append(str(len(count)))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()