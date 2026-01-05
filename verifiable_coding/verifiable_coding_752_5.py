import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split(b'\n')
    data = input[0].split()
    N = int(data[0])
    Q = int(data[1])
    mappings = {}
    index = 2
    for _ in range(N):
        ext = input[index].split()[0]
        media = input[index].split()[1]
        mappings[ext] = media
        index += 1
    for _ in range(Q):
        filename = input[index].decode()
        index += 1
        if '.' in filename:
            ext = filename.split('.')[-1]
            if ext in mappings:
                print(mappings[ext])
            else:
                print("unknown")
        else:
            print("unknown")

if __name__ == '__main__':
    solve()