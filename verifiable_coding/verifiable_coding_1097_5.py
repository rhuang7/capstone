import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        L = int(data[idx])
        B = int(data[idx + 1])
        idx += 2
        # Initialize the cake dimensions
        l, b = L, B
        # Track if Sinchan gets to eat
        sinchan_gets = False
        # Track the area Sinchan gets
        sinchan_area = 0
        # Process each friend
        for i in range(N):
            # Determine the largest square that can be cut
            side = min(l, b)
            # The area of the square is side * side
            square_area = side * side
            # The remaining area is (l * b - square_area)
            # The remaining cake is (l - side) * b or l * (b - side)
            # Update the cake dimensions
            if l > b:
                l -= side
            else:
                b -= side
            # Check if the cake is empty
            if l <= 0 and b <= 0:
                break
            # Check if the cake is a square
            if l == b:
                sinchan_gets = True
                sinchan_area = l * b
                break
        # Check if Sinchan gets to eat
        if sinchan_gets:
            results.append(f"Yes {sinchan_area}")
        else:
            results.append("No")
    # Print all results
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()