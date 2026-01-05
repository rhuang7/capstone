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
        
        # Check if it's possible to create a string with F(s, t) <= k
        # The maximum possible F(s, t) is len(s), so if k < 0, it's impossible
        if k < 0:
            results.append("NOPE")
            continue
        
        # Get unique characters in s
        unique_s = set(s)
        len_s = len(s)
        
        # If k is greater than or equal to len_s, return the lex smallest string of len_s with unique chars
        if k >= len_s:
            # Generate lex smallest string of len_s with unique chars
            res = ""
            for c in "abcdefghijklmnopqrstuvwxyz":
                if len(res) < len_s:
                    res += c
                else:
                    break
            results.append(res)
            continue
        
        # Otherwise, try to find the lex smallest string t with F(s, t) <= k
        # We need to include at most k characters from s, and the rest from other characters
        # We can use a greedy approach: include the smallest possible characters not in s, and then include the smallest possible characters from s that are not already included
        
        # Get characters not in s
        not_in_s = [c for c in "abcdefghijklmnopqrstuvwxyz" if c not in unique_s]
        
        # Sort not_in_s lexicographically
        not_in_s.sort()
        
        # Get characters in s
        in_s = sorted(unique_s)
        
        # We can include up to k characters from s
        # We need to include as many as possible from not_in_s, and then include the smallest possible characters from s that are not already included
        
        # Start with the smallest characters not in s
        t = []
        used_in_s = set()
        count_in_s = 0
        
        # Add as many as possible from not_in_s
        for c in not_in_s:
            t.append(c)
            if len(t) == len_s:
                break
        
        # Now add the smallest possible characters from s that are not already used
        for c in in_s:
            if len(t) < len_s and c not in used_in_s:
                t.append(c)
                used_in_s.add(c)
                count_in_s += 1
                if count_in_s == k:
                    break
        
        # If the length of t is less than len_s, add the remaining characters from s
        while len(t) < len_s:
            for c in in_s:
                if c not in used_in_s:
                    t.append(c)
                    used_in_s.add(c)
                    break
        
        # Check if the number of characters from s is <= k
        count_in_s = len(used_in_s)
        if count_in_s > k:
            results.append("NOPE")
        else:
            results.append("".join(t))
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()