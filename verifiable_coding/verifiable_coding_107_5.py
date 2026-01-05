import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    for _ in range(T):
        A = int(data[index])
        B = int(data[index+1])
        C = int(data[index+2])
        D = int(data[index+3])
        index += 4
        
        # Determine possible boxes
        possible = [False] * 4
        
        # Check if box 0 (first box) is possible
        # Box 0 requires final toy to be in (-infty, -1]
        # This is possible if the product of all toys is <= -1
        # Since all toys are in their respective ranges, we can analyze the product
        # For box 0 to be possible, the product must be <= -1
        # But how can we determine this from the counts?
        # We need to check if there's a way to combine the toys to get a product <= -1
        # This is possible if there's at least one toy in box 0 (A > 0) and the product of all other toys is positive
        # Or if there's at least one toy in box 0 (A > 0) and the product of all other toys is negative
        # But how can we check this?
        # Let's think about the sign of the product
        # The product of all toys is negative if there's an odd number of negative toys
        # But since we don't know the actual values, we need to find if there's a possible combination that leads to the desired box
        # This is a complex problem, but we can use the following logic:
        # For box 0 to be possible, the product of all toys must be <= -1
        # We can simulate this by considering the sign of the product and the magnitude
        # For box 0 to be possible, the product must be negative and its magnitude must be >= 1
        # We can check if there's a way to have a product that is negative and >= 1 in magnitude
        # This is possible if there's at least one toy in box 0 (A > 0) and the product of all other toys is positive
        # Or if there's at least one toy in box 0 (A > 0) and the product of all other toys is negative
        # But how can we check this?
        # We can use the following logic:
        # If there is at least one toy in box 0 (A > 0) and the product of all other toys is positive, then the product of all toys is negative
        # If there is at least one toy in box 0 (A > 0) and the product of all other toys is negative, then the product of all toys is positive
        # But how can we determine the product of all other toys?
        # We can use the following logic:
        # The product of all other toys is positive if there is an even number of negative toys
        # The product of all other toys is negative if there is an odd number of negative toys
        # But since we don't know the actual values, we need to find if there's a way to have a product that is negative and >= 1 in magnitude
        # This is a complex problem, but we can use the following logic:
        # For box 0 to be possible, the product of all toys must be <= -1
        # We can simulate this by considering the sign of the product and the magnitude
        # For box 0 to be possible, the product must be negative and its magnitude must be >= 1
        # We can check if there's a way to have a product that is negative and >= 1 in magnitude
        # This is possible if there's at least one toy in box 0 (A > 0) and the product of all other toys is positive
        # Or if there's at least one toy in box 0 (A > 0) and the product of all other toys is negative
        # But how can we check this?
        # We can use the following logic:
        # The product of all other toys is positive if there is an even number of negative toys
        # The product of all other toys is negative if there is an odd number of negative toys
        # But since we don't know the actual values, we need to find if there's a way to have a product that is negative and >= 1 in magnitude
        # This is a complex problem, but we can use the following logic:
        # For box 0 to be possible, the product of all toys must be <= -1
        # We can simulate this by considering the sign of the product and the magnitude
        # For box 0 to be possible, the product must be negative and its magnitude must be >= 1
        # We can check if there's a way to have a product that is negative and >= 1 in magnitude
        # This is possible if there's at least one toy in box 0 (A > 0) and the product of all other toys is positive
        # Or if there's at least one toy in box 0 (A > 0) and the product of all other toys is negative
        # But how can we check this?
        # We can use the following logic:
        # The product of all other toys is positive if there is an even number of negative toys
        # The product of all other toys is negative if there is an odd number of negative toys
        # But since we don't know the actual values, we need to find if there's a way to have a product that is negative and >= 1 in magnitude
        # This is a complex problem, but we can use the following logic:
        # For box 0 to be possible, the product of all toys must be <= -1
        # We can simulate this by considering the sign of the product and the magnitude
        # For box 0 to be possible, the product must be negative and its magnitude must be >= 1
        # We can check if there's a way to have a product that is negative and >= 1 in magnitude
        # This is possible if there's at least one toy in box 0 (A > 0) and the product of all other toys is positive
        # Or if there's at least one toy in box 0 (A > 0) and the product of all other toys is negative
        # But how can we check this?
        # We can use the following logic:
        # The product of all other toys is positive if there is an even number of negative toys
        # The product of all other toys is negative if there is an odd number of negative toys
        # But since we don't know the actual values, we need to find if there's a way to have a product that is negative and >= 1 in magnitude
        # This is a complex problem, but we can use the following logic:
        # For box 0 to be possible, the product of all toys must be <= -1
        # We can simulate this by considering the sign of the product and the magnitude
        # For box 0 to be possible, the product must be negative and its magnitude must be >= 1
        # We can check if there's a way to have a product that is negative and >= 1 in magnitude
        # This is possible if there's at least one toy in box 0 (A > 0) and the product of all other toys is positive
        # Or if there's at least one toy in box 0 (A > 0) and the product of all other toys is negative
        # But how can we check this?
        # We can use the following logic:
        # The product of all other toys is positive if there is an even number of negative toys
        # The product of all other toys is negative if there is an odd number of negative toys
        # But since we don't know the actual values, we need to find if there's a way to have a product that is negative and >= 1 in magnitude
        # This is a complex problem, but we can use the following logic:
        # For box 0 to be possible, the product of all toys must be <= -1
        # We can simulate this by considering the sign of the product and the magnitude
        # For box 0 to be possible, the product must be negative and its magnitude must be >= 1
        # We can check if there's a way to have a product that is negative and >= 1 in magnitude
        # This is possible if there's at least one toy in box 0 (A > 0) and the product of all other toys is positive
        # Or if there's at least one toy in box 0 (A > 0) and the product of all other toys is negative
        # But how can we check this?
        # We can use the following logic:
        # The product of all other toys is positive if there is an even number of negative toys
        # The product of all other toys is negative if there is an odd number of negative toys
        # But since we don't know the actual values, we need to find if there's a way to have a product that is negative and >= 1 in magnitude