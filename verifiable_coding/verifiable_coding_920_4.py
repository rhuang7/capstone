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
        
        # Precompute prefix sums for girls and boys
        prefix_girls = [0] * (len(s) + 1)
        prefix_boys = [0] * (len(s) + 1)
        
        for j in range(len(s)):
            prefix_girls[j + 1] = prefix_girls[j] + (1 if s[j] == 'g' else 0)
            prefix_boys[j + 1] = prefix_boys[j] + (1 if s[j] == 'b' else 0)
        
        # Calculate the minimum awkwardness
        # We will arrange boys and girls in a way that minimizes the sum of distances
        # We can use the formula for the optimal arrangement of boys and girls
        # The optimal arrangement is to place all girls first, then all boys or vice versa
        # We calculate both possibilities and choose the minimum
        
        # Option 1: all girls first, then all boys
        total = 0
        for i in range(len(s)):
            if s[i] == 'g':
                total += i * (girls - prefix_girls[i + 1]) + (prefix_boys[i + 1] - boys) * (len(s) - i)
            else:
                total += (prefix_girls[i + 1] - girls) * (i - (len(s) - boys)) + (len(s) - i) * (boys - prefix_boys[i + 1])
        
        # Option 2: all boys first, then all girls
        total2 = 0
        for i in range(len(s)):
            if s[i] == 'b':
                total2 += i * (boys - prefix_boys[i + 1]) + (prefix_girls[i + 1] - girls) * (len(s) - i)
            else:
                total2 += (prefix_boys[i + 1] - boys) * (i - (len(s) - girls)) + (len(s) - i) * (girls - prefix_girls[i + 1])
        
        results.append(min(total, total2))
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()