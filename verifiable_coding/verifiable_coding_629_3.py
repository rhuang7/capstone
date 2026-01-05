import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        R = int(data[idx])
        G = int(data[idx+1])
        B = int(data[idx+2])
        M = int(data[idx+3])
        idx +=4
        
        r = list(map(int, data[idx:idx+R]))
        idx += R
        g = list(map(int, data[idx:idx+G]))
        idx += G
        b = list(map(int, data[idx:idx+B]))
        idx += B
        
        # Sort each list in descending order
        r.sort(reverse=True)
        g.sort(reverse=True)
        b.sort(reverse=True)
        
        # Function to perform a magic trick on a list
        def apply_trick(arr, times):
            for _ in range(times):
                for i in range(len(arr)):
                    arr[i] //= 2
        
        # Apply tricks to each color
        # We can apply up to M tricks in total
        # We will try all possible combinations of tricks on the three colors
        # Since M is small (<=100), we can try all possible combinations
        
        # We will try all possible combinations of tricks on the three colors
        # with total tricks <= M
        # We will try all possible combinations of (tricks on red, tricks on green, tricks on blue)
        # such that tricks_red + tricks_green + tricks_blue <= M
        
        # We will keep track of the minimum possible maximum value
        min_max = float('inf')
        
        # Try all possible combinations of tricks
        for tricks_red in range(M+1):
            for tricks_green in range(M - tricks_red +1):
                tricks_blue = M - tricks_red - tricks_green
                if tricks_blue < 0:
                    continue
                # Make copies of the arrays to avoid modifying original
                r_copy = r[:]
                g_copy = g[:]
                b_copy = b[:]
                # Apply tricks
                apply_trick(r_copy, tricks_red)
                apply_trick(g_copy, tricks_green)
                apply_trick(b_copy, tricks_blue)
                # Compute maximum
                current_max = max(max(r_copy), max(g_copy), max(b_copy))
                if current_max < min_max:
                    min_max = current_max
        
        results.append(str(min_max))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()