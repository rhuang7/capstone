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
        count = 0
        word_to_bool = {}
        for _ in range(N):
            while idx < len(data) and data[idx].strip() == b'':
                idx += 1
            if idx >= len(data):
                break
            line = data[idx].strip().split()
            idx += 1
            w = line[0]
            s = int(line[1])
            if w in word_to_bool:
                if word_to_bool[w] != s:
                    continue
            word_to_bool[w] = s
            count += 1
        results.append(str(count))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()