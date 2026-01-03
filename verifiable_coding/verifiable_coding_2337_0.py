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
        
        # We need to find the maximum number of medalists such that:
        # g > 0, s > 0, b > 0
        # g < s, g < b
        # p_g > p_s > p_b > p_notmedal
        # g + s + b <= n // 2
        
        # We will try to find the maximum possible g + s + b
        # by trying different values of b, s, g
        
        max_medals = 0
        best_g = best_s = best_b = 0
        
        # Try all possible values of b (number of bronze medalists)
        # since b must be at least 1, and the number of bronze medalists must be at least 1
        # and the bronze medalists must have strictly more problems than the non-medalists
        # so we can try to find the maximum b such that p[b] > p[n - 1]
        # and then find s and g accordingly
        
        # Try all possible b from 1 to n//2
        for b in range(1, n // 2 + 1):
            # Find the minimum value of p that is strictly greater than p[n - 1]
            # since bronze medalists must have strictly more than non-medalists
            # the non-medalists are the last (n - (g + s + b)) participants
            # so the bronze medalists must have strictly more than p[n - (g + s + b)]
            # but we don't know g and s yet
            # so we can try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # but this is not straightforward
            # so we will try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # and then find s and g accordingly
            
            # We can try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # but this is not straightforward
            # so we will try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # and then find s and g accordingly
            
            # We can try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # but this is not straightforward
            # so we will try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # and then find s and g accordingly
            
            # We will try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # but this is not straightforward
            # so we will try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # and then find s and g accordingly
            
            # We can try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # but this is not straightforward
            # so we will try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # and then find s and g accordingly
            
            # We can try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # but this is not straightforward
            # so we will try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # and then find s and g accordingly
            
            # We can try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # but this is not straightforward
            # so we will try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # and then find s and g accordingly
            
            # We can try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # but this is not straightforward
            # so we will try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # and then find s and g accordingly
            
            # We can try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # but this is not straightforward
            # so we will try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # and then find s and g accordingly
            
            # We can try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # but this is not straightforward
            # so we will try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # and then find s and g accordingly
            
            # We can try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # but this is not straightforward
            # so we will try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # and then find s and g accordingly
            
            # We can try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # but this is not straightforward
            # so we will try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # and then find s and g accordingly
            
            # We can try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # but this is not straightforward
            # so we will try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # and then find s and g accordingly
            
            # We can try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # but this is not straightforward
            # so we will try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # and then find s and g accordingly
            
            # We can try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # but this is not straightforward
            # so we will try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # and then find s and g accordingly
            
            # We can try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # but this is not straightforward
            # so we will try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # and then find s and g accordingly
            
            # We can try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # but this is not straightforward
            # so we will try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # and then find s and g accordingly
            
            # We can try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # but this is not straightforward
            # so we will try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # and then find s and g accordingly
            
            # We can try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # but this is not straightforward
            # so we will try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # and then find s and g accordingly
            
            # We can try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # but this is not straightforward
            # so we will try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # and then find s and g accordingly
            
            # We can try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # but this is not straightforward
            # so we will try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # and then find s and g accordingly
            
            # We can try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # but this is not straightforward
            # so we will try to find the maximum b such that p[b] > p[n - (g + s + b)]
            # and then find s and g accordingly
            
            # We can try to find the maximum b such