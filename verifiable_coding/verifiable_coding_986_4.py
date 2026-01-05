import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        N = int(data[index])
        K = int(data[index + 1])
        index += 2
        
        if K == 0:
            print(' '.join(map(str, range(1, N + 1))))
            continue
        
        if N % 2 == 1:
            if K == 0:
                print(' '.join(map(str, range(1, N + 1))))
            else:
                print("CAPTAIN AMERICA EVADES")
            continue
        
        if K == 1:
            res = []
            for i in range(1, N + 1):
                if i % 2 == 1:
                    res.append(i + 1)
                else:
                    res.append(i - 1)
            print(' '.join(map(str, res)))
        else:
            print("CAPTAIN AMERICA EVADES")

if __name__ == '__main__':
    solve()