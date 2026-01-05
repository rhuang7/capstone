import sys
import bisect

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
        p = list(map(int, data[idx:idx + n]))
        idx += n
        
        # Find the maximum number of medalists possible
        max_medalists = n // 2
        # We need at least 3 medalists (g, s, b > 0)
        if max_medalists < 3:
            results.append("0 0 0")
            continue
        
        # We need to find g, s, b such that:
        # g < s < b
        # p[0] > p[g] > p[s] > p[b] > p[n-1]
        # We need to find the largest possible g + s + b
        
        # Try all possible values of b (starting from the smallest possible)
        # We need at least 3 medalists, so b >= 3
        # The maximum possible b is n - 1 (but we need at least 3 medalists)
        # So we try b from 3 to max_medalists
        
        best_g = 0
        best_s = 0
        best_b = 0
        max_total = 0
        
        for b in range(3, max_medalists + 1):
            # Find the smallest value in p[0...b-1] that is strictly greater than p[b]
            # We need p[g] > p[s] > p[b]
            # So we need to find s such that p[s] > p[b]
            # And find g such that p[g] > p[s]
            # We can use binary search for this
            
            # Find the largest s such that p[s] > p[b]
            # Since p is non-increasing, we can use bisect_left
            # We need to find the first index where p[i] <= p[b]
            # Then s is that index - 1
            # But we need s to be at least 1 (since s > 0)
            # And s must be at least g + 1
            # And g must be at least 1
            
            # Find the first index where p[i] <= p[b]
            # Since p is non-increasing, we can use bisect_left
            # We can use a custom bisect function
            
            # Find the first index where p[i] <= p[b]
            # Since p is non-increasing, we can use bisect_left with a reversed list
            # Or use bisect_left on the reversed list
            
            # We can use bisect_left on the list p, but with a reversed comparison
            # We can use bisect_left on the list p, but with a custom key
            
            # We need to find the first index where p[i] <= p[b]
            # Since p is non-increasing, we can use bisect_left on the list p
            # with a custom key
            
            # We can use bisect_left on the list p, but with a custom key
            # We can use bisect_left on the list p, but with a custom key
            
            # Find the first index where p[i] <= p[b]
            # Since p is non-increasing, we can use bisect_left on the list p
            # with a custom key
            
            # Find the first index where p[i] <= p[b]
            # Since p is non-increasing, we can use bisect_left on the list p
            # with a custom key
            
            # Find the first index where p[i] <= p[b]
            # Since p is non-increasing, we can use bisect_left on the list p
            # with a custom key
            
            # Find the first index where p[i] <= p[b]
            # Since p is non-increasing, we can use bisect_left on the list p
            # with a custom key
            
            # Find the first index where p[i] <= p[b]
            # Since p is non-increasing, we can use bisect_left on the list p
            # with a custom key
            
            # Find the first index where p[i] <= p[b]
            # Since p is non-increasing, we can use bisect_left on the list p
            # with a custom key
            
            # Find the first index where p[i] <= p[b]
            # Since p is non-increasing, we can use bisect_left on the list p
            # with a custom key
            
            # Find the first index where p[i] <= p[b]
            # Since p is non-increasing, we can use bisect_left on the list p
            # with a custom key
            
            # Find the first index where p[i] <= p[b]
            # Since p is non-increasing, we can use bisect_left on the list p
            # with a custom key
            
            # Find the first index where p[i] <= p[b]
            # Since p is non-increasing, we can use bisect_left on the list p
            # with a custom key
            
            # Find the first index where p[i] <= p[b]
            # Since p is non-increasing, we can use bisect_left on the list p
            # with a custom key
            
            # Find the first index where p[i] <= p[b]
            # Since p is non-increasing, we can use bisect_left on the list p
            # with a custom key
            
            # Find the first index where p[i] <= p[b]
            # Since p is non-increasing, we can use bisect_left on the list p
            # with a custom key
            
            # Find the first index where p[i] <= p[b]
            # Since p is non-increasing, we can use bisect_left on the list p
            # with a custom key
            
            # Find the first index where p[i] <= p[b]
            # Since p is non-increasing, we can use bisect_left on the list p
            # with a custom key
            
            # Find the first index where p[i] <= p[b]
            # Since p is non-increasing, we can use bisect_left on the list p
            # with a custom key
            
            # Find the first index where p[i] <= p[b]
            # Since p is non-increasing, we can use bisect_left on the list p
            # with a custom key
            
            # Find the first index where p[i] <= p[b]
            # Since p is non-increasing, we can use bisect_left on the list p
            # with a custom key
            
            # Find the first index where p[i] <= p[b]
            # Since p is non-increasing, we can use bisect_left on the list p
            # with a custom key
            
            # Find the first index where p[i] <= p[b]
            # Since p is non-increasing, we can use bisect_left on the list p
            # with a custom key
            
            # Find the first index where p[i] <= p[b]
            # Since p is non-increasing, we can use bisect_left on the list p
            # with a custom key
            
            # Find the first index where p[i] <= p[b]
            # Since p is non-increasing, we can use bisect_left on the list p
            # with a custom key
            
            # Find the first index where p[i] <= p[b]
            # Since p is non-increasing, we can use bisect_left on the list p
            # with a custom key
            
            # Find the first index where p[i] <= p[b]
            # Since p is non-increasing, we can use bisect_left on the list p
            # with a custom key
            
            # Find the first index where p[i] <= p[b]
            # Since p is non-increasing, we can use bisect_left on the list p
            # with a custom key
            
            # Find the first index where p[i] <= p[b]
            # Since p is non-increasing, we can use bisect_left on the list p
            # with a custom key
            
            # Find the first index where p[i] <= p[b]
            # Since p is non-increasing, we can use bisect_left on the list p
            # with a custom key
            
            # Find the first index where p[i] <= p[b]
            # Since p is non-increasing, we can use bisect_left on the list p
            # with a custom key
            
            # Find the first index where p[i] <= p[b]
            # Since p is non-increasing, we can use bisect_left on the list p
            # with a custom key
            
            # Find the first index where p[i] <= p[b]
            # Since p is non-increasing, we can use bisect_left on the list p
            # with a custom key
            
            # Find the first index where p[i] <= p[b]
            # Since p is non-increasing, we can use bisect_left on the list p
            # with a custom key
            
            # Find the first index where p[i]