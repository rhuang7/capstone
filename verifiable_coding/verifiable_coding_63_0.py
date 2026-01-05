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
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        w = list(map(int, data[idx:idx+k]))
        idx += k
        
        a.sort()
        w.sort()
        
        # To maximize the sum of happiness, we need to:
        # 1. Assign the largest numbers to the friends with the most integers (so their max is large)
        # 2. Assign the smallest numbers to the friends with the most integers (so their min is small)
        # But since each friend gets exactly w_i integers, we need to balance the max and min
        
        # We will use a greedy approach:
        # - Assign the largest numbers to the friends with the largest w_i (so their max is large)
        # - Assign the smallest numbers to the friends with the largest w_i (so their min is small)
        
        # We will sort the friends by w_i in descending order
        # Then, for each friend, assign the largest available number as max, and the smallest available as min
        # But since each friend gets exactly w_i integers, we need to assign w_i - 1 numbers in between
        
        # So, for each friend, we take the largest available number as max, and the smallest available as min
        # Then, we take w_i - 2 numbers in between (they don't affect the happiness)
        
        # So, the total happiness is sum of (max + min) for each friend
        
        # We will use two pointers: left (smallest available) and right (largest available)
        # We will assign the largest available as max, and the smallest available as min
        # Then, we take w_i - 2 numbers in between (they don't affect the happiness)
        
        left = 0
        right = n - 1
        total = 0
        
        # Sort the friends by w_i in descending order
        friends = sorted(zip(w, range(k)), key=lambda x: -x[0])
        
        for w_i, _ in friends:
            # Assign the largest available as max
            max_val = a[right]
            # Assign the smallest available as min
            min_val = a[left]
            total += (max_val + min_val)
            # Move pointers
            right -= 1
            left += 1
        
        results.append(str(total))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()