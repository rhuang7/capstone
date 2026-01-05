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
        n = int(data[idx])
        idx += 1
        s = data[idx]
        idx += 1
        x = list(map(int, data[idx:idx + n]))
        idx += n
        
        # Find positions of villages with electricity
        electrified = []
        for i in range(n):
            if s[i] == '1':
                electrified.append(x[i])
        
        # The villages without electricity are in between the electrified ones
        # We need to connect them with the minimum total wire length
        # The optimal way is to connect each un-electrified village to the nearest electrified one
        # So we can iterate through the villages and for each un-electrified one, find the closest electrified one
        
        # To optimize, we can use a two-pointer approach
        left = 0
        right = 0
        total = 0
        
        while left < len(electrified):
            # Find the first un-electrified village after the current electrified one
            while right < len(x) and s[right] == '1':
                right += 1
            if right >= len(x):
                break
            # Now, right is the first un-electrified village
            # Find the closest electrified village to the right
            # Since the villages are sorted, we can use binary search
            # But since we are moving left and right pointers, we can just compare with the current electrified one
            # and the next one
            if left + 1 < len(electrified):
                # Compare with current and next electrified village
                dist1 = x[right] - electrified[left]
                dist2 = electrified[left + 1] - x[right]
                total += min(dist1, dist2)
            else:
                # Only one electrified village, connect to it
                total += x[right] - electrified[left]
            left += 1
            right += 1
        
        results.append(str(total))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()