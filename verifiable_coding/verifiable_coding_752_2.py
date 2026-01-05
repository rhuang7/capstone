import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split(b'\n')
    idx = 0
    NQ = input[idx].split()
    idx += 1
    N = int(NQ[0])
    Q = int(NQ[1])
    ext_to_type = {}
    for _ in range(N):
        if idx >= len(input):
            break
        line = input[idx].split()
        idx += 1
        if len(line) < 2:
            continue
        ext = line[0].decode()
        typ = line[1].decode()
        ext_to_type[ext] = typ
    for _ in range(Q):
        if idx >= len(input):
            break
        line = input[idx].split()
        idx += 1
        filename = line[0].decode()
        if '.' not in filename:
            print("unknown")
            continue
        parts = filename.split('.')
        ext = parts[-1]
        if ext in ext_to_type:
            print(ext_to_type[ext])
        else:
            print("unknown")

if __name__ == '__main__':
    solve()