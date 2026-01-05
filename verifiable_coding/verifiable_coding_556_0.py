import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    t_list = list(map(int, data[1:]))
    
    for t in t_list:
        if t == 0:
            print("0 0")
            continue
        # Determine the side length of the square the t-th step is in
        n = 1
        while n * 4 <= t:
            n += 1
        n -= 1
        # Calculate the remaining steps after completing the square of side n
        rem = t - (n * (n - 1))
        # Determine which side of the square the remaining steps are on
        if rem <= n:
            # First side: up
            x, y = -rem + 1, n
        elif rem <= 2 * n:
            # Second side: left
            x, y = -n, rem - n
        elif rem <= 3 * n:
            # Third side: down
            x, y = rem - 2 * n, -n
        else:
            # Fourth side: right
            x, y = n, rem - 3 * n
        print(f"{x} {y}")

if __name__ == '__main__':
    solve()