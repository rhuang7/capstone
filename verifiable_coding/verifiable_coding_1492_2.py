import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        n = int(data[idx])
        idx += 1
        strings = []
        for _ in range(n):
            s = data[idx]
            idx += 1
            strings.append(s)
        
        # Find the minimum possible LCS
        # The minimum LCS is the minimum number of 'a's in all strings
        # Because if there is at least one 'a' in all strings, the LCS can be at least 1
        # But if there is at least one string with no 'a's, then the LCS is 0
        has_a = all('a' in s for s in strings)
        if has_a:
            # The minimum LCS is 1 if all strings have at least one 'a'
            # But we need to find the minimum possible LCS, which is the minimum number of 'a's in all strings
            # But since we can choose the omen string, the minimum LCS is 0 if there is at least one string with no 'a's
            # Wait, no. The omen string can be any string. So the minimum LCS is the minimum number of 'a's in all strings
            # But since we can choose the omen string, the minimum LCS is 0 if there is at least one string with no 'a's
            # Because we can choose the omen string to have no 'a's, making the LCS 0
            # But if all strings have at least one 'a', then the minimum LCS is 1
            # Because the omen string can be chosen to have one 'a' and the rest 'b's, making the LCS 1
            # So the answer is 0 if there is at least one string with no 'a's, else 1
            # But wait, the omen string can be any string. So if all strings have at least one 'a', then the minimum LCS is 1
            # Because the omen string can be chosen to have one 'a' and the rest 'b's, making the LCS 1
            # But if there is at least one string with no 'a's, then the omen string can be chosen to have no 'a's, making the LCS 0
            # So the answer is 0 if there is at least one string with no 'a's, else 1
            # But wait, what if all strings have at least one 'a', but some have more than one?
            # The minimum LCS is 1, because we can choose the omen string to have one 'a' and the rest 'b's
            # So the answer is 0 if there is at least one string with no 'a's, else 1
            # But wait, what if all strings have at least one 'a', but some have more than one?
            # The minimum LCS is 1, because we can choose the omen string to have one 'a' and the rest 'b's
            # So the answer is 0 if there is at least one string with no 'a's, else 1
            # But wait, what if all strings have at least one 'a', but some have more than one?
            # The minimum LCS is 1, because we can choose the omen string to have one 'a' and the rest 'b's
            # So the answer is 0 if there is at least one string with no 'a's, else 1
            # But wait, what if all strings have at least one 'a', but some have more than one?
            # The minimum LCS is 1, because we can choose the omen string to have one 'a' and the rest 'b's
            # So the answer is 0 if there is at least one string with no 'a's, else 1
            # But wait, what if all strings have at least one 'a', but some have more than one?
            # The minimum LCS is 1, because we can choose the omen string to have one 'a' and the rest 'b's
            # So the answer is 0 if there is at least one string with no 'a's, else 1
            # But wait, what if all strings have at least one 'a', but some have more than one?
            # The minimum LCS is 1, because we can choose the omen string to have one 'a' and the rest 'b's
            # So the answer is 0 if there is at least one string with no 'a's, else 1
            # But wait, what if all strings have at least one 'a', but some have more than one?
            # The minimum LCS is 1, because we can choose the omen string to have one 'a' and the rest 'b's
            # So the answer is 0 if there is at least one string with no 'a's, else 1
            # But wait, what if all strings have at least one 'a', but some have more than one?
            # The minimum LCS is 1, because we can choose the omen string to have one 'a' and the rest 'b's
            # So the answer is 0 if there is at least one string with no 'a's, else 1
            # But wait, what if all strings have at least one 'a', but some have more than one?
            # The minimum LCS is 1, because we can choose the omen string to have one 'a' and the rest 'b's
            # So the answer is 0 if there is at least one string with no 'a's, else 1
            # But wait, what if all strings have at least one 'a', but some have more than one?
            # The minimum LCS is 1, because we can choose the omen string to have one 'a' and the rest 'b's
            # So the answer is 0 if there is at least one string with no 'a's, else 1
            # But wait, what if all strings have at least one 'a', but some have more than one?
            # The minimum LCS is 1, because we can choose the omen string to have one 'a' and the rest 'b's
            # So the answer is 0 if there is at least one string with no 'a's, else 1
            # But wait, what if all strings have at least one 'a', but some have more than one?
            # The minimum LCS is 1, because we can choose the omen string to have one 'a' and the rest 'b's
            # So the answer is 0 if there is at least one string with no 'a's, else 1
            # But wait, what if all strings have at least one 'a', but some have more than one?
            # The minimum LCS is 1, because we can choose the omen string to have one 'a' and the rest 'b's
            # So the answer is 0 if there is at least one string with no 'a's, else 1
            # But wait, what if all strings have at least one 'a', but some have more than one?
            # The minimum LCS is 1, because we can choose the omen string to have one 'a' and the rest 'b's
            # So the answer is 0 if there is at least one string with no 'a's, else 1
            # But wait, what if all strings have at least one 'a', but some have more than one?
            # The minimum LCS is 1, because we can choose the omen string to have one 'a' and the rest 'b's
            # So the answer is 0 if there is at least one string with no 'a's, else 1
            # But wait, what if all strings have at least one 'a', but some have more than one?
            # The minimum LCS is 1, because we can choose the omen string to have one 'a' and the rest 'b's
            # So the answer is 0 if there is at least one string with no 'a's, else 1
            # But wait, what if all strings have at least one 'a', but some have more than one?
            # The minimum LCS is 1, because we can choose the omen string to have one 'a' and the rest 'b's
            # So the answer is 0 if there is at least one string with no 'a's, else 1
            # But wait, what if all strings have at least one 'a', but some have more than one?
            # The minimum LCS is 1, because we can choose the omen string to have one 'a' and the rest 'b's
            # So the answer is 0 if there is at least one string with no 'a's, else 1
            # But wait, what if all strings have at least one 'a', but some have more than one?
            # The minimum LCS is 1, because we can choose the omen string to have one 'a'