import sys

def solve():
    import math
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        N = int(data[index])
        index += 1
        x = int(data[index])
        y = int(data[index+1])
        z = int(data[index+2])
        index += 3
        
        # Calculate the number of times each group comes
        cnt_x = (N * x) // x
        cnt_y = (N * y) // y
        cnt_z = (N * z) // z
        
        # The number of times all three groups come is the minimum of the counts
        result = min(cnt_x, cnt_y, cnt_z)
        print(result)

if __name__ == '__main__':
    solve()