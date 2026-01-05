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
        max1 = max(A, B, C)
        min1 = min(A, B, C)
        second_largest = (A + B + C) - max1 - min1
        print(second_largest)

if __name__ == '__main__':
    solve()