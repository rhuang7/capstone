import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split(b'\n')
    
    first_line = data[0].split()
    N = int(first_line[0])
    Q = int(first_line[1])
    
    media_types = {}
    index = 1
    for _ in range(N):
        if index >= len(data):
            break
        line = data[index].split()
        if len(line) < 2:
            index += 1
            continue
        ext = line[0].decode()
        media = line[1].decode()
        media_types[ext] = media
        index += 1
    
    for _ in range(Q):
        if index >= len(data):
            break
        line = data[index].split()
        if len(line) < 1:
            index += 1
            continue
        filename = line[0].decode()
        index += 1
        
        # Extract extension
        if '.' in filename:
            parts = filename.split('.', 1)
            ext = parts[1]
            if ext in media_types:
                print(media_types[ext])
            else:
                print("unknown")
        else:
            print("unknown")

if __name__ == '__main__':
    solve()