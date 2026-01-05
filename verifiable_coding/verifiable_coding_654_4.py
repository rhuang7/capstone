import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        A = int(data[index])
        B = int(data[index+1])
        C = int(data[index+2])
        index += 3
        # Find second largest
        if A >= B and A >= C:
            if B >= C:
                print(B)
            else:
                print(C)
        elif B >= A and B >= C:
            if A >= C:
                print(A)
            else:
                print(C)
        else:
            if A >= B:
                print(A)
            else:
                print(B)

if __name__ == '__main__':
    solve()