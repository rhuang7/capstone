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
        s = data[index]
        index += 1
        t = data[index]
        index += 1
        
        # Check if s and t are already equal
        if s == t:
            print("YES")
            continue
        
        # Check if the multiset of characters in s and t are the same
        from collections import Counter
        if Counter(s) != Counter(t):
            print("NO")
            continue
        
        # Check if the number of differing positions is even
        diff = 0
        for a, b in zip(s, t):
            if a != b:
                diff += 1
        if diff % 2 != 0:
            print("NO")
            continue
        
        # If all conditions are satisfied, it is possible
        print("YES")

if __name__ == '__main__':
    solve()