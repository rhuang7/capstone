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
        current = None
        while i < len(s):
            if s[i] == '1':
                if current is None:
                    current = ('square', 1)
                    i += 1
                else:
                    if current[0] == 'square':
                        current = ('square', current[1] + 1)
                    else:
                        if current[1] == 1:
                            print(0)
                            break
                        else:
                            print(0)
                            break
            else:
                if current is None:
                    print(0)
                    break
                else:
                    if current[0] == 'square':
                        if current[1] == 1:
                            print(0)
                            break
                        else:
                            if current[1] % 2 == 0:
                                print(current[1] // 2)
                            else:
                                print(0)
                            break
                    else:
                        if current[1] == 1:
                            print(0)
                            break
                        else:
                            if current[1] % 2 == 0:
                                print(current[1] // 2)
                            else:
                                print(0)
                            break
            i += 1
        else:
            if current is not None and current[0] == 'square':
                print(1)
            else:
                print(0)

if __name__ == '__main__':
    solve()