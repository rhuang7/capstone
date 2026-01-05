import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    cases = list(map(int, data[1:t+1]))
    
    def is_nice(n):
        # Check if a staircase with n stairs is nice
        # A staircase with n stairs has total cells = 1 + 2 + ... + n = n*(n+1)/2
        # For it to be nice, the total cells must be a triangular number and also satisfy the condition that the sum of the first k terms of the sequence 1, 3, 5, ... is equal to the triangular number
        # The sequence of nice staircases is 1, 3, 5, 7, ...
        # So n must be odd
        if n % 2 == 0:
            return False
        return True
    
    def count_nice_up_to(x):
        # Count the number of nice staircases that can be built with total cells <= x
        count = 0
        total = 0
        i = 1
        while True:
            if is_nice(i):
                cells = i * (i + 1) // 2
                if total + cells > x:
                    break
                total += cells
                count += 1
            i += 1
        return count
    
    for x in cases:
        print(count_nice_up_to(x))

if __name__ == '__main__':
    solve()