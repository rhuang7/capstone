import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        s = data[index]
        k = int(data[index + 1])
        index += 2
        
        used = set(s)
        available = [c for c in 'abcdefghijklmnopqrstuvwxyz' if c not in used]
        used_chars = set(s)
        used_chars_sorted = sorted(used_chars)
        available_sorted = sorted(available)
        
        # Find the lex smallest string t with len(s) characters, all unique, and F(s, t) <= k
        # F(s, t) is the number of common characters between s and t
        # So we need to choose at most k characters from s, and the rest from available characters
        
        # We need to select exactly len(s) characters, with at most k from s
        # So we need to select (len(s) - k) characters from available, and k from s
        # But we need to choose the lex smallest string, so we need to choose the smallest possible characters
        
        # Get the characters from s sorted
        s_sorted = sorted(s)
        # Get the characters from available sorted
        available_sorted = sorted(available)
        
        # We need to select (len(s) - k) characters from available_sorted, and k from s_sorted
        # But we need to choose the lex smallest string, so we need to choose the smallest possible characters
        
        # Choose the smallest (len(s) - k) characters from available_sorted
        available_part = available_sorted[:len(s) - k]
        # Choose the smallest k characters from s_sorted
        s_part = s_sorted[:k]
        
        # Combine them and sort to get the lex smallest string
        result = sorted(available_part + s_part)
        result_str = ''.join(result)
        
        # Check if the result has length len(s)
        if len(result_str) != len(s):
            print("NOPE")
        else:
            print(result_str)
            
if __name__ == '__main__':
    solve()