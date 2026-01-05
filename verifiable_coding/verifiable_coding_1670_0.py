import sys

def solve():
    reserved = {' ': '%20', '!': '%21', '$': '%24', '%': '%25', '(': '%28', ')': '%29', '*': '%2a'}
    data = sys.stdin.buffer.read().split(b'\n')
    for line in data:
        if line == b'#':
            break
        s = line.decode('utf-8')
        result = ''
        for c in s:
            if c in reserved:
                result += reserved[c]
            else:
                result += c
        print(result)

if __name__ == '__main__':
    solve()