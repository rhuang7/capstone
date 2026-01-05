import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    N = int(input[0])
    strings = input[1:N+1]

    for s in strings:
        if not s:
            print(0)
            continue
        i = 0
        current = 0
        while i < len(s):
            if s[i] == '1':
                if current == 0:
                    current = 1
                else:
                    if current % 2 == 1:
                        current += 1
                    else:
                        current = 1
                i += 1
            else:
                if current == 0:
                    current = 1
                else:
                    if current % 2 == 1:
                        current += 1
                    else:
                        current = 1
                i += 1
        print(current // 2)

if __name__ == '__main__':
    solve()