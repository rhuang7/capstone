import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    x_list = list(map(int, data[1:t+1]))
    
    def is_nice(n):
        # A staircase with n stairs is nice if the sum of the first n triangular numbers is a triangular number
        # The sum of the first n triangular numbers is n(n+1)(n+2)/6
        # We check if this sum is a triangular number, i.e., exists k such that k(k+1)/2 = n(n+1)(n+2)/6
        # Rearranging, we get k(k+1) = n(n+1)(n+2)
        # We can solve this equation for k
        # The solution is k = (n^2 + 3n + 2 - sqrt((n^2 + 3n + 2)^2 - 8n(n+1)(n+2))) / 2
        # But instead of solving this, we can check for k such that k(k+1)/2 = n(n+1)(n+2)/6
        # So we compute the sum and check if it is a triangular number
        sum_tri = n * (n + 1) * (n + 2) // 6
        # Check if sum_tri is a triangular number
        # k(k+1)/2 = sum_tri => k^2 + k - 2*sum_tri = 0
        # Solve for k
        # k = [-1 + sqrt(1 + 8*sum_tri)] / 2
        sqrt_val = (1 + 8 * sum_tri) ** 0.5
        k = (-1 + sqrt_val) / 2
        if k.is_integer():
            return True
        return False
    
    def count_nice_staircases(x):
        count = 0
        total = 0
        n = 1
        while True:
            if is_nice(n):
                cells = n * (n + 1) * (n + 2) // 6
                if total + cells <= x:
                    count += 1
                    total += cells
                else:
                    break
            else:
                # Check if we can add this staircase even though it's not nice
                # But according to the problem, only nice staircases are counted
                # So we skip it
                pass
            n += 1
        return count
    
    for x in x_list:
        print(count_nice_staircases(x))

if __name__ == '__main__':
    solve()