import sys

def solve():
    reserved = {' ': '%20', '!': '%21', '$': '%24', '%': '%25', '(': '%28', ')': '%29', '*': '%2a'}
    data = sys.stdin.buffer.read().decode()
    lines = data.strip().split('\n')
    for line in lines:
        if line == '#':
            break
        result = ''
        for char in line:
            if char in reserved:
                result += reserved[char]
            else:
                result += char
        print(result)

if __name__ == '__main__':
    solve()