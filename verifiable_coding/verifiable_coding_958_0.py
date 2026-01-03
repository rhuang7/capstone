import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    
    for k in cases:
        if k == 1:
            print("*")
        elif k == 2:
            print("*")
            print("* *")
        elif k == 3:
            print("*")
            print("* *")
            print("*****")
        elif k == 4:
            print("*")
            print("* *")
            print("*   *")
            print("*******")
        elif k == 5:
            print("*")
            print("* *")
            print("*   *")
            print("*     *")
            print("*********")
        else:
            for i in range(1, k+1):
                if i == 1:
                    print("*")
                elif i == 2:
                    print("* *")
                else:
                    spaces = ' ' * (i-2)
                    print("*" + spaces + "*")
            for i in range(k-1, 0, -1):
                if i == 1:
                    print("*")
                elif i == 2:
                    print("* *")
                else:
                    spaces = ' ' * (i-2)
                    print("*" + spaces + "*")

if __name__ == '__main__':
    solve()