import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]
    
    def count_good_substrings(s):
        n = len(s)
        count = 0
        
        # Check for substrings of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                count += 1
        
        # Check for substrings of length > 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                # Check the middle part for single distinct character
                j = i + 2
                k = i + 2
                while j < k:
                    if s[j] != s[k]:
                        break
                    j += 1
                    k -= 1
                else:
                    count += 1
        
        return count
    
    for s in cases:
        print(count_good_substrings(s))

if __name__ == '__main__':
    solve()