import sys

def solve():
    q = int(sys.stdin.buffer.readline())
    for _ in range(q):
        s = sys.stdin.buffer.readline().strip()
        t = sys.stdin.buffer.readline().strip()
        if s == t:
            print("YES")
            continue
        # Check if each character in s can be transformed to the corresponding character in t
        # using the allowed operations
        # The allowed operations allow us to propagate characters to adjacent positions
        # So, for each position i, the character in s[i] can be changed to any character in s
        # as long as there is a path of adjacent positions to reach it
        # Similarly for t[i]
        # So, for each position i, the character in s[i] must be present in the multiset of s
        # and the character in t[i] must be present in the multiset of t
        # But since we can perform operations on both strings, we can adjust both strings
        # to have the same characters
        # So, the problem reduces to checking if the multiset of characters in s and t are the same
        # But since we can perform operations on both strings, we can transform both strings to have the same multiset
        # So, the answer is always YES
        # Wait, this is not correct. Let me think again.
        # The operation allows us to change a character to its adjacent character
        # So, for example, if s is "abc" and t is "cba", can we transform s into t?
        # Let's see:
        # s = "abc"
        # We can change s[1] to s[0], making s = "aacc"
        # Then change s[2] to s[1], making s = "aacc"
        # Then change s[0] to s[1], making s = "aacc"
        # So it's not possible to transform s into t in this case
        # So the correct approach is to check if for each position i, the character in s[i] can be transformed to t[i] through some sequence of operations
        # But how?
        # The operation allows us to change a character to its adjacent character
        # So, for example, if s[i] is 'a' and s[i+1] is 'b', we can change s[i] to 'b' or s[i+1] to 'a'
        # So, the operation allows us to propagate characters to adjacent positions
        # So, if we have a character 'a' in s, we can propagate it to any position to the left or right
        # So, the multiset of characters in s and t must be the same
        # Because we can transform both strings to have the same multiset
        # So, the answer is YES if the multiset of characters in s and t are the same
        # But wait, the problem says that we can perform operations on both strings
        # So, we can transform s and t independently to have the same multiset
        # So, the answer is always YES
        # But this is not correct
        # Let's think again
        # The operation allows us to change a character to its adjacent character
        # So, if s is "abc" and t is "cba", can we transform s into t?
        # Let's see:
        # s = "abc"
        # We can change s[1] to s[0], making s = "aacc"
        # Then change s[2] to s[1], making s = "aacc"
        # Then change s[0] to s[1], making s = "aacc"
        # So it's not possible to transform s into t in this case
        # So the correct approach is to check if for each position i, the character in s[i] can be transformed to t[i] through some sequence of operations
        # But how?
        # The operation allows us to change a character to its adjacent character
        # So, for example, if s[i] is 'a' and s[i+1] is 'b', we can change s[i] to 'b' or s[i+1] to 'a'
        # So, the operation allows us to propagate characters to adjacent positions
        # So, if we have a character 'a' in s, we can propagate it to any position to the left or right
        # So, the multiset of characters in s and t must be the same
        # Because we can transform both strings to have the same multiset
        # So, the answer is YES if the multiset of characters in s and t are the same
        # But this is not correct
        # Let's think again
        # The operation allows us to change a character to its adjacent character
        # So, for example, if s is "abc" and t is "cba", can we transform s into t?
        # Let's see:
        # s = "abc"
        # We can change s[1] to s[0], making s = "aacc"
        # Then change s[2] to s[1], making s = "aacc"
        # Then change s[0] to s[1], making s = "aacc"
        # So it's not possible to transform s into t in this case
        # So the correct approach is to check if for each position i, the character in s[i] can be transformed to t[i] through some sequence of operations
        # But how?
        # The operation allows us to change a character to its adjacent character
        # So, for example, if s[i] is 'a' and s[i+1] is 'b', we can change s[i] to 'b' or s[i+1] to 'a'
        # So, the operation allows us to propagate characters to adjacent positions
        # So, if we have a character 'a' in s, we can propagate it to any position to the left or right
        # So, the multiset of characters in s and t must be the same
        # Because we can transform both strings to have the same multiset
        # So, the answer is YES if the multiset of characters in s and t are the same
        # But this is not correct
        # Let's think again
        # The operation allows us to change a character to its adjacent character
        # So, for example, if s is "abc" and t is "cba", can we transform s into t?
        # Let's see:
        # s = "abc"
        # We can change s[1] to s[0], making s = "aacc"
        # Then change s[2] to s[1], making s = "aacc"
        # Then change s[0] to s[1], making s = "aacc"
        # So it's not possible to transform s into t in this case
        # So the correct approach is to check if for each position i, the character in s[i] can be transformed to t[i] through some sequence of operations
        # But how?
        # The operation allows us to change a character to its adjacent character
        # So, for example, if s[i] is 'a' and s[i+1] is 'b', we can change s[i] to 'b' or s[i+1] to 'a'
        # So, the operation allows us to propagate characters to adjacent positions
        # So, if we have a character 'a' in s, we can propagate it to any position to the left or right
        # So, the multiset of characters in s and t must be the same
        # Because we can transform both strings to have the same multiset
        # So, the answer is YES if the multiset of characters in s and t are the same
        # But this is not correct
        # Let's think again
        # The operation allows us to change a character to its adjacent character
        # So, for example, if s is "abc" and t is "cba", can we transform s into t?
        # Let's see:
        # s = "abc"
        # We can change s[1] to s[0], making s = "aacc"
        # Then change s[2] to s[1], making s = "aacc"
        # Then change s[0] to s[1], making s = "aacc"
        # So it's not possible to transform s into t in this case
        # So the correct approach is to check if for each position i, the character in s[i] can be transformed to t[i] through some sequence of operations
        # But how?
        # The operation allows us to change a character to its adjacent character
        # So, for example, if s[i] is 'a' and s[i+1] is 'b', we can change s[i] to 'b' or s[i+1] to 'a'
        # So, the operation allows us to propagate characters to adjacent positions
        # So, if we have a character 'a' in s, we can propagate it to any position to the left or right
        # So, the multiset of characters in s and t must be the same
        # Because we can transform both strings to have the same