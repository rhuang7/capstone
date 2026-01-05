import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    cases = list(map(int, data[1:t+1]))
    
    def is_nice(n):
        # Check if a staircase with n stairs is nice
        # The total number of cells in a staircase with n stairs is sum(1..n) = n*(n+1)/2
        # For it to be nice, the sum must be a triangular number and the number of cells must be a square number
        # But according to the problem statement, a staircase is nice if it can be covered by n disjoint squares
        # The condition for a staircase with n stairs to be nice is that n is a triangular number
        # So we check if n is a triangular number
        # Solve for k in k*(k+1)/2 = n
        # k^2 + k - 2n = 0
        # k = [-1 + sqrt(1 + 8n)] / 2
        # k must be an integer
        k = (1 + int((1 + 8 * n) ** 0.5)) // 2
        return k * (k + 1) // 2 == n
    
    def count_nice_up_to(x):
        # Count the number of nice staircases that can be built with total cells <= x
        count = 0
        total = 0
        n = 1
        while True:
            cells = n * (n + 1) // 2
            if total + cells > x:
                break
            if is_nice(n):
                count += 1
            total += cells
            n += 1
        return count
    
    for x in cases:
        print(count_nice_up_to(x))

if __name__ == '__main__':
    solve()