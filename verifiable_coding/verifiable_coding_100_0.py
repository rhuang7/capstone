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
        
        # Sort the counts
        a, b, c = sorted([r, g, b])
        
        # The maximum number of days is determined by the sum of the two smaller piles
        # minus the largest pile, but not less than the sum of the two smaller piles
        # divided by 2 (since each day requires two candies)
        max_days = (a + b) // 2
        if a + b > c:
            max_days = min(max_days, (a + b + c) // 2)
        else:
            max_days = min(max_days, (a + b + c) // 2)
        
        results.append(str(max_days))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()