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
        
        # Check if s and t have the same character counts
        from collections import Counter
        if Counter(s) != Counter(t):
            print("NO")
            continue
        
        # Check if the first and last characters are the same
        if s[0] != t[0] or s[-1] != t[-1]:
            print("NO")
            continue
        
        # Check if the middle characters can be rearranged
        # We can perform any number of reverses, so we can sort the middle part
        # If the middle parts of s and t can be rearranged, then it's possible
        # So we check if the sorted middle parts are equal
        # But since we can reverse any substring, we can sort the entire string
        # So we check if the sorted s and t are equal
        if sorted(s) == sorted(t):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()