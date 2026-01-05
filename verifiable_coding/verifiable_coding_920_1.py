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
        # Starting with 'b' if there are more boys, otherwise start with 'g'
        # We can calculate the minimum awkwardness by considering the positions of boys and girls
        
        # Precompute prefix sums for girls and boys
        prefix_girls = [0] * (len(s) + 1)
        prefix_boys = [0] * (len(s) + 1)
        
        for j in range(len(s)):
            prefix_girls[j + 1] = prefix_girls[j] + (1 if s[j] == 'g' else 0)
            prefix_boys[j + 1] = prefix_boys[j] + (1 if s[j] == 'b' else 0)
        
        # Calculate the minimum awkwardness
        min_awkwardness = 0
        pos = 0
        if boys > girls:
            # Start with 'b'
            for i in range(len(s)):
                if i % 2 == 0:
                    min_awkwardness += (i + 1) - (pos + 1)
                    pos += 1
                else:
                    min_awkwardness += (i + 1) - (pos + 1)
                    pos += 1
        else:
            # Start with 'g'
            for i in range(len(s)):
                if i % 2 == 0:
                    min_awkwardness += (i + 1) - (pos + 1)
                    pos += 1
                else:
                    min_awkwardness += (i + 1) - (pos + 1)
                    pos += 1
        
        results.append(str(min_awkwardness))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()