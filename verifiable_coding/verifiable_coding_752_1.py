import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split(b'\n')
    idx = 0
    NQ = input[idx].split()
    idx += 1
    N = int(NQ[0])
    Q = int(NQ[1])
    media_types = {}
    for _ in range(N):
        if idx >= len(input):
            break
        line = input[idx].split()
        idx += 1
        if len(line) < 2:
            continue
        ext = line[0].decode('utf-8')
        media = line[1].decode('utf-8')
        media_types[ext] = media
    for _ in range(Q):
        if idx >= len(input):
            break
        line = input[idx].split()
        idx += 1
        filename = line[0].decode('utf-8')
        if '.' not in filename:
            print("unknown")
            continue
        ext = filename.split('.')[-1]
        print(media_types.get(ext, "unknown"))

if __name__ == '__main__':
    solve()