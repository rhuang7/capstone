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
        
        # The optimal arrangement is to place all boys and girls alternately
        # starting with the one that has more count to minimize the distance
        if boys >= girls:
            # Start with 'b'
            arrangement = ['b'] * boys + ['g'] * girls
        else:
            # Start with 'g'
            arrangement = ['g'] * girls + ['b'] * boys
        
        # Compute the awkwardness
        awkwardness = 0
        for i in range(len(arrangement)):
            for j in range(i + 1, len(arrangement)):
                if arrangement[i] != arrangement[j]:
                    awkwardness += abs(i - j)
        
        results.append(str(awkwardness))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()