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
        
        # Check if s and t can be made equal with the allowed operations
        # The allowed operations allow us to reverse any substring of the same length in s and t
        # This means we can perform any number of reverses on s and t, as long as the lengths are the same
        # So, the problem reduces to whether s and t can be transformed into each other using any number of reverses
        
        # Since any number of reverses can be done, the only thing that matters is whether s and t have the same multiset of characters
        # But since the problem allows us to reverse any substring, we can rearrange the characters in s and t as needed
        # So the answer is YES if s and t have the same characters (count of each character)
        
        # But wait, the operation is to reverse a substring of s and a substring of t of the same length
        # So, the operation is not just any permutation of characters, but a specific type of transformation
        # However, since we can perform any number of such operations, the key insight is that the parity of the number of character differences between s and t must be even
        
        # But this is not sufficient. The correct approach is to check if s and t are anagrams (same multiset of characters)
        # Because with the allowed operations, we can perform any number of reverses on s and t, which allows us to rearrange the characters
        
        # So the correct condition is: s and t must be anagrams
        if sorted(s) == sorted(t):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()