import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        N = int(data[index])
        K = int(data[index+1])
        index += 2
        if K == 0:
            print(' '.join(map(str, range(1, N+1))))
            continue
        if N % 2 == 1:
            if K == 0:
                print(' '.join(map(str, range(1, N+1))))
            else:
                print("CAPTAIN AMERICA EVADES")
        else:
            if K == 0:
                print(' '.join(map(str, range(1, N+1))))
            else:
                if K == 1:
                    arr = [i for i in range(1, N+1)]
                    for i in range(N//2):
                        arr[i], arr[N-1-i] = arr[N-1-i], arr[i]
                    print(' '.join(map(str, arr)))
                else:
                    print("CAPTAIN AMERICA EVADES")

if __name__ == '__main__':
    solve()