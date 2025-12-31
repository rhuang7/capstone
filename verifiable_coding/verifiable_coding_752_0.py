import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split(b'\n')
    
    first_line = data[0].split()
    N = int(first_line[0])
    Q = int(first_line[1])
    
    media_types = {}
    
    for i in range(1, N + 1):
        if i >= len(data):
            break
        line = data[i].split()
        if len(line) < 2:
            continue
        ext = line[0].decode()
        media = line[1].decode()
        media_types[ext] = media
    
    for i in range(N + 1, len(data)):
        if i >= len(data):
            break
        line = data[i].split()
        if not line:
            continue
        filename = line[0].decode()
        if '.' not in filename:
            print("unknown")
            continue
        parts = filename.split('.', 1)
        ext = parts[1]
        if ext in media_types:
            print(media_types[ext])
        else:
            print("unknown")

if __name__ == '__main__':
    solve()