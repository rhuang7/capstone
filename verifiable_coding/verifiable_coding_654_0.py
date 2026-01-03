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
        if A >= B:
            if B >= C:
                second_largest = B
            else:
                second_largest = C
        else:
            if A >= C:
                second_largest = A
            else:
                second_largest = C
        
        print(second_largest)

if __name__ == '__main__':
    solve()