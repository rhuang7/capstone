import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    index = 1
    for _ in range(t):
        n = int(data[index])
        m = int(data[index+1])
        a = int(data[index+2])
        b = int(data[index+3])
        index += 4
        
        # Check if the total number of ones is consistent
        total_ones = n * a
        if total_ones % m != 0:
            print("NO")
            continue
        if total_ones != m * b:
            print("NO")
            continue
        
        # Check if it's possible to arrange the ones
        if (n * a) % m != 0 or (m * b) % n != 0:
            print("NO")
            continue
        
        # Create the matrix
        matrix = []
        for i in range(n):
            row = ['0'] * m
            ones_placed = 0
            for j in range(m):
                if ones_placed < a:
                    row[j] = '1'
                    ones_placed += 1
            matrix.append(''.join(row))
        
        print("YES")
        for row in matrix:
            print(row)
        
if __name__ == '__main__':
    solve()