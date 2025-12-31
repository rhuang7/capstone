import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    cases = list(map(int, data[1:t+1]))
    
    def is_nice(n):
        # A staircase with n stairs is nice if the sum of the first n triangular numbers is a perfect square
        # The total number of cells in a staircase with n stairs is sum_{i=1 to n} i*(i+1)/2 = n(n+1)(n+2)/6
        # We need this to be a perfect square
        total = n * (n + 1) * (n + 2) // 6
        return int(total**0.5)**2 == total
    
    def count_nice_up_to(x):
        count = 0
        total_cells = 0
        n = 1
        while True:
            cells = n * (n + 1) * (n + 2) // 6
            if total_cells + cells > x:
                break
            if is_nice(n):
                count += 1
            total_cells += cells
            n += 1
        return count
    
    for x in cases:
        print(count_nice_up_to(x))

if __name__ == '__main__':
    solve()