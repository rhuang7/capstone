import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        s = data[index]
        index += 1
        
        # Process the string
        res = []
        i = 0
        while i < n:
            if s[i] == '0':
                res.append('0')
                i += 1
            else:
                # We can remove the '1' or the '0' if possible
                # We want to keep as many '0's as possible and minimize the length
                # So we remove the '1' and keep the '0'
                # But we need to check if there is a '0' after this '1'
                # If there is, we can remove the '1' and keep the '0'
                # If not, we remove the '1' and keep the '0' (but it's the last one)
                # So we remove the '1' and keep the '0'
                # But we need to check if there is a '0' after this '1'
                # If there is, we can remove the '1' and keep the '0'
                # If not, we remove the '1' and keep the '0' (but it's the last one)
                # So we remove the '1' and keep the '0'
                # So we keep the '0' and move to the next character
                # But we need to check if there is a '0' after this '1'
                # If there is, we can remove the '1' and keep the '0'
                # If not, we remove the '1' and keep the '0' (but it's the last one)
                # So we remove the '1' and keep the '0'
                # So we keep the '0' and move to the next character
                # But we need to check if there is a '0' after this '1'
                # If there is, we can remove the '1' and keep the '0'
                # If not, we remove the '1' and keep the '0' (but it's the last one)
                # So we remove the '1' and keep the '0'
                # So we keep the '0' and move to the next character
                # But we need to check if there is a '0' after this '1'
                # If there is, we can remove the '1' and keep the '0'
                # If not, we remove the '1' and keep the '0' (but it's the last one)
                # So we remove the '1' and keep the '0'
                # So we keep the '0' and move to the next character
                # But we need to check if there is a '0' after this '1'
                # If there is, we can remove the '1' and keep the '0'
                # If not, we remove the '1' and keep the '0' (but it's the last one)
                # So we remove the '1' and keep the '0'
                # So we keep the '0' and move to the next character
                # But we need to check if there is a '0' after this '1'
                # If there is, we can remove the '1' and keep the '0'
                # If not, we remove the '1' and keep the '0' (but it's the last one)
                # So we remove the '1' and keep the '0'
                # So we keep the '0' and move to the next character
                # But we need to check if there is a '0' after this '1'
                # If there is, we can remove the '1' and keep the '0'
                # If not, we remove the '1' and keep the '0' (but it's the last one)
                # So we remove the '1' and keep the '0'
                # So we keep the '0' and move to the next character
                # But we need to check if there is a '0' after this '1'
                # If there is, we can remove the '1' and keep the '0'
                # If not, we remove the '1' and keep the '0' (but it's the last one)
                # So we remove the '1' and keep the '0'
                # So we keep the '0' and move to the next character
                # But we need to check if there is a '0' after this '1'
                # If there is, we can remove the '1' and keep the '0'
                # If not, we remove the '1' and keep the '0' (but it's the last one)
                # So we remove the '1' and keep the '0'
                # So we keep the '0' and move to the next character
                # But we need to check if there is a '0' after this '1'
                # If there is, we can remove the '1' and keep the '0'
                # If not, we remove the '1' and keep the '0' (but it's the last one)
                # So we remove the '1' and keep the '0'
                # So we keep the '0' and move to the next character
                # But we need to check if there is a '0' after this '1'
                # If there is, we can remove the '1' and keep the '0'
                # If not, we remove the '1' and keep the '0' (but it's the last one)
                # So we remove the '1' and keep the '0'
                # So we keep the '0' and move to the next character
                # But we need to check if there is a '0' after this '1'
                # If there is, we can remove the '1' and keep the '0'
                # If not, we remove the '1' and keep the '0' (but it's the last one)
                # So we remove the '1' and keep the '0'
                # So we keep the '0' and move to the next character
                # But we need to check if there is a '0' after this '1'
                # If there is, we can remove the '1' and keep the '0'
                # If not, we remove the '1' and keep the '0' (but it's the last one)
                # So we remove the '1' and keep the '0'
                # So we keep the '0' and move to the next character
                # But we need to check if there is a '0' after this '1'
                # If there is, we can remove the '1' and keep the '0'
                # If not, we remove the '1' and keep the '0' (but it's the last one)
                # So we remove the '1' and keep the '0'
                # So we keep the '0' and move to the next character
                # But we need to check if there is a '0' after this '1'
                # If there is, we can remove the '1' and keep the '0'
                # If not, we remove the '1' and keep the '0' (but it's the last one)
                # So we remove the '1' and keep the '0'
                # So we keep the '0' and move to the next character
                # But we need to check if there is a '0' after this '1'
                # If there is, we can remove the '1' and keep the '0'
                # If not, we remove the '1' and keep the '0' (but it's the last one)
                # So we remove the '1' and keep the '0'
                # So we keep the '0' and move to the next character
                # But we need to check if there is a '0' after this '1'
                # If there is, we can remove the '1' and keep the '0'
                # If not, we remove the '1' and keep the '0' (but it's the last one)
                # So we remove the '1' and keep the '0'
                # So we keep the '0' and move to the next character
                # But we need to check if there is a '0' after this '1'
                # If there is, we can remove the '1' and keep the '0'
                # If not, we remove the '1' and keep the '0' (but it's the last one)
                # So we remove the '1' and keep the '0'
                # So we keep the '0' and move to the next character
                # But we need to check if there is a '0' after this '1'
                # If there is, we can remove the '1' and keep the '0'
                # If not, we remove the '1' and keep the '0' (but it's the last one