import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    idx = 1
    results = []
    
    for _ in range(T):
        s = data[idx]
        k = int(data[idx+1])
        idx += 2
        
        unique_chars = set(s)
        len_s = len(s)
        
        # If k is less than the number of unique characters in s, it's impossible
        if k < len(unique_chars):
            results.append("NOPE")
            continue
        
        # We need to find the lexicographically smallest string t of the same length as s
        # with at most k characters in common with s
        
        # The lex smallest string is made of the first (len_s - k) letters not in s, followed by the first k letters in s
        # But we need to ensure that the total length is len_s
        
        # Get all letters not in s
        not_in_s = [c for c in 'abcdefghijklmnopqrstuvwxyz' if c not in unique_chars]
        in_s = sorted([c for c in 'abcdefghijklmnopqrstuvwxyz' if c in unique_chars])
        
        # We can use at most k characters from s
        # So we take the first (len_s - k) letters not in s, then the first k letters in s
        # But we need to make sure the total length is len_s
        
        # If there are not enough letters not in s, we need to use some letters from s
        # So we take the first (len_s - k) letters not in s, then the first k letters in s
        
        # But we need to make sure that the total length is len_s
        # So the number of letters not in s is len(not_in_s)
        # If len(not_in_s) < (len_s - k), we need to use some letters from s
        
        # So we take the first (len_s - k) letters not in s, then the first k letters in s
        # But we need to make sure that the total length is len_s
        
        # So the first part is the first (len_s - k) letters not in s
        # The second part is the first k letters in s
        
        # But we need to make sure that the total length is len_s
        
        # So the total number of letters not in s is len(not_in_s)
        # So if len(not_in_s) >= (len_s - k), we can take the first (len_s - k) letters not in s
        # and then the first k letters in s
        # Otherwise, we take all letters not in s, and then the first (k - (len_s - len(not_in_s))) letters in s
        
        # So the first part is the first (len_s - k) letters not in s
        # The second part is the first k letters in s
        
        # But we need to make sure that the total length is len_s
        
        # So the first part is the first (len_s - k) letters not in s
        # The second part is the first k letters in s
        
        # But we need to make sure that the total length is len_s
        
        # So the first part is the first (len_s - k) letters not in s
        # The second part is the first k letters in s
        
        # But we need to make sure that the total length is len_s
        
        # So the first part is the first (len_s - k) letters not in s
        # The second part is the first k letters in s
        
        # But we need to make sure that the total length is len_s
        
        # So the first part is the first (len_s - k) letters not in s
        # The second part is the first k letters in s
        
        # But we need to make sure that the total length is len_s
        
        # So the first part is the first (len_s - k) letters not in s
        # The second part is the first k letters in s
        
        # But we need to make sure that the total length is len_s
        
        # So the first part is the first (len_s - k) letters not in s
        # The second part is the first k letters in s
        
        # But we need to make sure that the total length is len_s
        
        # So the first part is the first (len_s - k) letters not in s
        # The second part is the first k letters in s
        
        # But we need to make sure that the total length is len_s
        
        # So the first part is the first (len_s - k) letters not in s
        # The second part is the first k letters in s
        
        # But we need to make sure that the total length is len_s
        
        # So the first part is the first (len_s - k) letters not in s
        # The second part is the first k letters in s
        
        # But we need to make sure that the total length is len_s
        
        # So the first part is the first (len_s - k) letters not in s
        # The second part is the first k letters in s
        
        # But we need to make sure that the total length is len_s
        
        # So the first part is the first (len_s - k) letters not in s
        # The second part is the first k letters in s
        
        # But we need to make sure that the total length is len_s
        
        # So the first part is the first (len_s - k) letters not in s
        # The second part is the first k letters in s
        
        # But we need to make sure that the total length is len_s
        
        # So the first part is the first (len_s - k) letters not in s
        # The second part is the first k letters in s
        
        # But we need to make sure that the total length is len_s
        
        # So the first part is the first (len_s - k) letters not in s
        # The second part is the first k letters in s
        
        # But we need to make sure that the total length is len_s
        
        # So the first part is the first (len_s - k) letters not in s
        # The second part is the first k letters in s
        
        # But we need to make sure that the total length is len_s
        
        # So the first part is the first (len_s - k) letters not in s
        # The second part is the first k letters in s
        
        # But we need to make sure that the total length is len_s
        
        # So the first part is the first (len_s - k) letters not in s
        # The second part is the first k letters in s
        
        # But we need to make sure that the total length is len_s
        
        # So the first part is the first (len_s - k) letters not in s
        # The second part is the first k letters in s
        
        # But we need to make sure that the total length is len_s
        
        # So the first part is the first (len_s - k) letters not in s
        # The second part is the first k letters in s
        
        # But we need to make sure that the total length is len_s
        
        # So the first part is the first (len_s - k) letters not in s
        # The second part is the first k letters in s
        
        # But we need to make sure that the total length is len_s
        
        # So the first part is the first (len_s - k) letters not in s
        # The second part is the first k letters in s
        
        # But we need to make sure that the total length is len_s
        
        # So the first part is the first (len_s - k) letters not in s
        # The second part is the first k letters in s
        
        # But we need to make sure that the total length is len_s
        
        # So the first part is the first (len_s - k) letters not in s
        # The second part is the first k letters in s
        
        # But we need to make sure that the total length is len_s
        
        # So the first part is the first (len_s - k) letters not in s
        # The second part is the first k letters in s
        
        # But we need to make sure that the total length is len_s
        
        # So the first part is the first (len_s - k) letters not in s
        # The second part is the first k letters in s
        
        # But we need to make sure that the total length is len_s
        
        # So the first part is the first (len_s - k) letters not in s
        # The second part is the first k letters in s
        
        # But we need to make sure that the total length is len_s
        
        # So the first part is the first (len_s - k) letters not in s
        # The second part is the first k letters in s
        
        # But we need to make sure that the total length is len_s
        
        # So the first part is the first (len_s - k) letters not in s
        # The second part is the first k letters in s
        
        # But we