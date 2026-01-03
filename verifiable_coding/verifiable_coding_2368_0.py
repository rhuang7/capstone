import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        b = list(map(int, data[idx:idx + n]))
        idx += n
        
        # Find the minimum moves required
        # For each gift, we can reduce a_i and b_i to some value (x, y)
        # We need to find x and y such that all a_i and b_i can be reduced to x and y
        # The optimal x is the minimum of a_i, and the optimal y is the minimum of b_i
        # But since we can also reduce both a_i and b_i by 1 at the same time, we need to find the best way to balance
        
        # The optimal x is the minimum of a_i, and the optimal y is the minimum of b_i
        # But we can also reduce both a_i and b_i by 1 at the same time, so we need to find the best way to balance
        
        # The minimum moves is the sum of (a_i - x) + (b_i - y) - (number of times we can reduce both a_i and b_i by 1)
        # But x and y must be such that x <= a_i and y <= b_i for all i
        
        # The optimal x is the minimum of a_i, and the optimal y is the minimum of b_i
        # But we can also reduce both a_i and b_i by 1 at the same time, so we need to find the best way to balance
        
        # So we need to find x and y such that x <= a_i and y <= b_i for all i, and the total moves is minimized
        
        # The optimal x is the minimum of a_i, and the optimal y is the minimum of b_i
        # But we can also reduce both a_i and b_i by 1 at the same time, so we need to find the best way to balance
        
        # The minimum moves is the sum of (a_i - x) + (b_i - y) - (number of times we can reduce both a_i and b_i by 1)
        # But x and y must be such that x <= a_i and y <= b_i for all i
        
        # The optimal x is the minimum of a_i, and the optimal y is the minimum of b_i
        # But we can also reduce both a_i and b_i by 1 at the same time, so we need to find the best way to balance
        
        # So we need to find x and y such that x <= a_i and y <= b_i for all i, and the total moves is minimized
        
        # The optimal x is the minimum of a_i, and the optimal y is the minimum of b_i
        # But we can also reduce both a_i and b_i by 1 at the same time, so we need to find the best way to balance
        
        # The minimum moves is the sum of (a_i - x) + (b_i - y) - (number of times we can reduce both a_i and b_i by 1)
        # But x and y must be such that x <= a_i and y <= b_i for all i
        
        # The optimal x is the minimum of a_i, and the optimal y is the minimum of b_i
        # But we can also reduce both a_i and b_i by 1 at the same time, so we need to find the best way to balance
        
        # So we need to find x and y such that x <= a_i and y <= b_i for all i, and the total moves is minimized
        
        # The optimal x is the minimum of a_i, and the optimal y is the minimum of b_i
        # But we can also reduce both a_i and b_i by 1 at the same time, so we need to find the best way to balance
        
        # The minimum moves is the sum of (a_i - x) + (b_i - y) - (number of times we can reduce both a_i and b_i by 1)
        # But x and y must be such that x <= a_i and y <= b_i for all i
        
        # The optimal x is the minimum of a_i, and the optimal y is the minimum of b_i
        # But we can also reduce both a_i and b_i by 1 at the same time, so we need to find the best way to balance
        
        # So we need to find x and y such that x <= a_i and y <= b_i for all i, and the total moves is minimized
        
        # The optimal x is the minimum of a_i, and the optimal y is the minimum of b_i
        # But we can also reduce both a_i and b_i by 1 at the same time, so we need to find the best way to balance
        
        # The minimum moves is the sum of (a_i - x) + (b_i - y) - (number of times we can reduce both a_i and b_i by 1)
        # But x and y must be such that x <= a_i and y <= b_i for all i
        
        # The optimal x is the minimum of a_i, and the optimal y is the minimum of b_i
        # But we can also reduce both a_i and b_i by 1 at the same time, so we need to find the best way to balance
        
        # So we need to find x and y such that x <= a_i and y <= b_i for all i, and the total moves is minimized
        
        # The optimal x is the minimum of a_i, and the optimal y is the minimum of b_i
        # But we can also reduce both a_i and b_i by 1 at the same time, so we need to find the best way to balance
        
        # The minimum moves is the sum of (a_i - x) + (b_i - y) - (number of times we can reduce both a_i and b_i by 1)
        # But x and y must be such that x <= a_i and y <= b_i for all i
        
        # The optimal x is the minimum of a_i, and the optimal y is the minimum of b_i
        # But we can also reduce both a_i and b_i by 1 at the same time, so we need to find the best way to balance
        
        # So we need to find x and y such that x <= a_i and y <= b_i for all i, and the total moves is minimized
        
        # The optimal x is the minimum of a_i, and the optimal y is the minimum of b_i
        # But we can also reduce both a_i and b_i by 1 at the same time, so we need to find the best way to balance
        
        # The minimum moves is the sum of (a_i - x) + (b_i - y) - (number of times we can reduce both a_i and b_i by 1)
        # But x and y must be such that x <= a_i and y <= b_i for all i
        
        # The optimal x is the minimum of a_i, and the optimal y is the minimum of b_i
        # But we can also reduce both a_i and b_i by 1 at the same time, so we need to find the best way to balance
        
        # So we need to find x and y such that x <= a_i and y <= b_i for all i, and the total moves is minimized
        
        # The optimal x is the minimum of a_i, and the optimal y is the minimum of b_i
        # But we can also reduce both a_i and b_i by 1 at the same time, so we need to find the best way to balance
        
        # The minimum moves is the sum of (a_i - x) + (b_i - y) - (number of times we can reduce both a_i and b_i by 1)
        # But x and y must be such that x <= a_i and y <= b_i for all i
        
        # The optimal x is the minimum of a_i, and the optimal y is the minimum of b_i
        # But we can also reduce both a_i and b_i by 1 at the same time, so we need to find the best way to balance
        
        # So we need to find x and y such that x <= a_i and y <= b_i for all i, and the total moves is minimized
        
        # The optimal x is the minimum of a_i, and the optimal y is the minimum of b_i
        # But we can also reduce both a_i and b_i by 1 at the same time, so we need to find the best way to balance
        
        # The minimum moves is the sum of (a_i - x) + (b_i - y) - (number of times we can reduce both a_i and b_i by 1)
        # But x and y must be such that x <= a_i and y <= b_i for all i
        
        # The optimal x is the minimum of a_i, and the optimal y is the minimum of b_i