import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        a = int(input[idx])
        b = int(input[idx+1])
        c = int(input[idx+2])
        idx += 3
        # Find second largest
        if a > b:
            if b > c:
                second_largest = b
            elif a > c:
                second_largest = c
            else:
                second_largest = a
        else:
            if a > c:
                second_largest = a
            elif b > c:
                second_largest = b
            else:
                second_largest = c
        print(second_largest)

if __name__ == '__main__':
    solve()