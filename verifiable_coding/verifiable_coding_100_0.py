import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(t):
        r = int(data[index])
        g = int(data[index+1])
        b = int(data[index+2])
        index += 3
        
        # Sort the counts to simplify logic
        a, b, c = sorted([r, g, b])
        
        # The maximum number of days is limited by two cases:
        # 1. The sum of the two smaller piles minus the largest pile (if the largest is more than the sum of the other two)
        # 2. The sum of all three piles divided by 2 (since each day eats two candies)
        # The answer is the minimum of these two values
        max_days = min((a + b - c), (a + b + c) // 2)
        results.append(str(max_days))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()