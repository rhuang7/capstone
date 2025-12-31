import sys

def solve():
    reserved = {' ': '%20', '!': '%21', '$': '%24', '%': '%25', '(': '%28', ')': '%29', '*': '%2a'}
    data = sys.stdin.buffer.read().split(b'\n')
    for line in data:
        if line == b'#':
            break
        s = line.decode('utf-8')
        res = ''
        for c in s:
            if c in reserved:
                res += reserved[c]
            else:
                res += c
        print(res)

if __name__ == '__main__':
    solve()