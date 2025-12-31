import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        s = data[i]
        boys = s.count('b')
        girls = len(s) - boys
        
        # To minimize the awkwardness, we should alternate between 'b' and 'g'
        # Starting with 'b' if there are more boys, else starting with 'g'
        # We can calculate the minimum awkwardness based on the positions of boys and girls
        
        # Calculate the minimum awkwardness
        # The formula for the minimum awkwardness when alternating is:
        # (number of boys * number of girls) * 2 - (number of boys + number of girls)
        # But we need to adjust based on the actual positions
        
        # Alternative approach:
        # Place all boys and girls in alternating positions
        # Calculate the total distance between each boy and girl
        
        # Create the optimal arrangement
        res = []
        b = 0
        g = 0
        for c in s:
            if c == 'b':
                b += 1
            else:
                g += 1
        
        # Determine the starting character
        start = 'b' if b >= g else 'g'
        
        # Create the optimal arrangement
        arr = []
        b_count = 0
        g_count = 0
        for i in range(len(s)):
            if (i % 2 == 0 and start == 'b') or (i % 2 == 1 and start == 'g'):
                arr.append('b')
                b_count += 1
            else:
                arr.append('g')
                g_count += 1
        
        # Calculate the awkwardness
        awkwardness = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] != arr[j]:
                    awkwardness += abs(i - j)
        
        results.append(str(awkwardness))
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()