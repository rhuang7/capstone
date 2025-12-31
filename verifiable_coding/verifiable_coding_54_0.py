import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    q = int(data[0])
    index = 1
    
    for _ in range(q):
        n = int(data[index])
        index += 1
        s = list(map(int, data[index:index + n]))
        index += n
        
        # Count the frequency of each power of two
        from collections import defaultdict
        count = defaultdict(int)
        for num in s:
            count[num] += 1
        
        # We need to reach 2048, which is 2^11
        # So we work backwards from 2048
        # For each power of two, we check if we can combine pairs to reach the next higher power
        current = 11  # 2^11 = 2048
        while current >= 0:
            # How many of this power do we have?
            cnt = count[1 << current]
            # How many pairs can we form?
            pairs = cnt // 2
            # Each pair can be combined into the next higher power
            count[1 << (current + 1)] += pairs
            # Update the count for this power
            count[1 << current] -= pairs * 2
            current -= 1
        
        # If we have at least one 2048, then it's possible
        if count[2048] >= 1:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()