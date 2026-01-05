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
        
        if s == t:
            print("YES")
            continue
        
        # Check if s and t have the same multiset of characters
        if sorted(s) != sorted(t):
            print("NO")
            continue
        
        # Check if there exists a position where s and t differ
        diff = False
        for i in range(n):
            if s[i] != t[i]:
                diff = True
                break
        
        if not diff:
            print("YES")
            continue
        
        # For the first differing position, check if there exists a way to fix it
        # We can reverse a substring in s and a substring in t to make them equal
        # So, we need to find a position where s[i] != t[i], and then check if there's a way to fix it
        # We can always do this by reversing a substring that includes the differing position
        # So, the answer is always YES if the multiset of characters is the same
        print("YES")
        
if __name__ == '__main__':
    solve()