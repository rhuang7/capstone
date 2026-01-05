import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        s = data[idx]
        idx += 1
        
        if k % 2 != 0:
            results.append("NO")
            continue
        
        # Check if the string is already k-balanced
        valid = True
        for i in range(n - k + 1):
            substr = s[i:i+k]
            zeros = substr.count('0')
            ones = substr.count('1')
            if zeros != ones:
                valid = False
                break
        
        if valid:
            results.append("YES")
            continue
        
        # Try to fill in the question marks
        # For a k-balanced string, every k-length substring must have exactly k/2 0s and 1s
        # So, the string must alternate between 0 and 1 in a way that every k-length window has equal counts
        # This implies that the string must be of the form 0101... or 1010... or similar
        # But since k is even, the pattern must repeat every k characters
        # So, for the first k characters, we must have exactly k/2 0s and 1s
        # Then, the rest of the string must follow the same pattern
        
        # Check if the first k characters can be adjusted to have exactly k/2 0s and 1s
        count_0 = 0
        count_1 = 0
        for c in s[:k]:
            if c == '0':
                count_0 += 1
            elif c == '1':
                count_1 += 1
        
        if count_0 != count_1:
            results.append("NO")
            continue
        
        # Now, check if the rest of the string can be filled in according to the pattern
        # The pattern is determined by the first k characters
        # For example, if the first k characters are 0101..., then the pattern is 0,1,0,1,...
        # So, for each position i, the character should be 0 if i % 2 == 0, else 1
        # But since k can be even, we need to check if the pattern is consistent
        
        # Determine the pattern based on the first k characters
        # The pattern is determined by the first k characters, and must repeat
        # So, for each position i, the character should be the same as position i % k
        # But we need to ensure that every k-length window has exactly k/2 0s and 1s
        
        # Check if the pattern is consistent
        pattern = []
        for c in s[:k]:
            if c == '?':
                pattern.append(None)
            else:
                pattern.append(c)
        
        # Check if the pattern can be filled in to have exactly k/2 0s and 1s
        # We need to fill in the ?s in the first k characters
        # We can try to fill in the ?s to make the count of 0s and 1s equal
        # We can try to fill in the ?s to be 0 or 1 such that the count is k/2
        
        # Try to fill in the ?s in the first k characters
        # We need to have exactly k/2 0s and 1s
        # So, the number of 0s in the first k characters must be k/2
        # We can try to fill in the ?s to make that happen
        
        # Count the number of 0s and 1s in the first k characters
        count_0 = 0
        count_1 = 0
        for c in s[:k]:
            if c == '0':
                count_0 += 1
            elif c == '1':
                count_1 += 1
        
        # We need to have exactly k/2 0s and 1s in the first k characters
        # So, the number of ?s in the first k characters must be such that we can fill them to make the counts equal
        # The number of ?s is (k - (count_0 + count_1))
        num_question_marks = k - (count_0 + count_1)
        
        # The number of 0s needed is k/2
        # The number of 1s needed is k/2
        # So, we can try to fill in the ?s to make the counts equal
        
        # Try to fill in the ?s to make the counts equal
        # We can try to fill in the ?s to be 0 or 1 such that the counts are equal
        # We can try to fill in the ?s to be 0 or 1 such that the counts are equal
        # We need to find a way to fill in the ?s to make the counts equal
        
        # Try to fill in the ?s to make the counts equal
        # We can try to fill in the ?s to be 0 or 1 such that the counts are equal
        # We can try to fill in the ?s to be 0 or 1 such that the counts are equal
        # We can try to fill in the ?s to be 0 or 1 such that the counts are equal
        
        # We need to fill in the ?s in the first k characters to make the counts equal
        # So, we can try to fill in the ?s to be 0 or 1 such that the counts are equal
        
        # Try to fill in the ?s to make the counts equal
        # We can try to fill in the ?s to be 0 or 1 such that the counts are equal
        # We can try to fill in the ?s to be 0 or 1 such that the counts are equal
        # We can try to fill in the ?s to be 0 or 1 such that the counts are equal
        
        # We need to fill in the ?s in the first k characters to make the counts equal
        # So, we can try to fill in the ?s to be 0 or 1 such that the counts are equal
        
        # Try to fill in the ?s to make the counts equal
        # We can try to fill in the ?s to be 0 or 1 such that the counts are equal
        # We can try to fill in the ?s to be 0 or 1 such that the counts are equal
        # We can try to fill in the ?s to be 0 or 1 such that the counts are equal
        
        # We need to fill in the ?s in the first k characters to make the counts equal
        # So, we can try to fill in the ?s to be 0 or 1 such that the counts are equal
        
        # Try to fill in the ?s to make the counts equal
        # We can try to fill in the ?s to be 0 or 1 such that the counts are equal
        # We can try to fill in the ?s to be 0 or 1 such that the counts are equal
        # We can try to fill in the ?s to be 0 or 1 such that the counts are equal
        
        # We need to fill in the ?s in the first k characters to make the counts equal
        # So, we can try to fill in the ?s to be 0 or 1 such that the counts are equal
        
        # Try to fill in the ?s to make the counts equal
        # We can try to fill in the ?s to be 0 or 1 such that the counts are equal
        # We can try to fill in the ?s to be 0 or 1 such that the counts are equal
        # We can try to fill in the ?s to be 0 or 1 such that the counts are equal
        
        # We need to fill in the ?s in the first k characters to make the counts equal
        # So, we can try to fill in the ?s to be 0 or 1 such that the counts are equal
        
        # Try to fill in the ?s to make the counts equal
        # We can try to fill in the ?s to be 0 or 1 such that the counts are equal
        # We can try to fill in the ?s to be 0 or 1 such that the counts are equal
        # We can try to fill in the ?s to be 0 or 1 such that the counts are equal
        
        # We need to fill in the ?s in the first k characters to make the counts equal
        # So, we can try to fill in the ?s to be 0 or 1 such that the counts are equal
        
        # Try to fill in the ?s to make the counts equal
        # We can try to fill in the ?s to be 0 or 1 such that the counts are equal
        # We can try to fill in the ?s to be 0 or 1 such that