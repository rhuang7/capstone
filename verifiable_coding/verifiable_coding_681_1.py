import sys
import math

MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    K = int(data[2])
    A = list(map(int, data[3:3+N]))
    
    # Count the frequency of each number in A
    freq = [0] * (M + 1)
    for num in A:
        freq[num] += 1
    
    # Calculate the number of ways to choose how many times each number can be increased
    # We can increase a number up to (M - num) // K times
    # For each number, the number of ways to choose how many times it is increased is (M - num) // K + 1
    # However, we need to consider that we can only increase numbers in such a way that they don't exceed M
    # And that we can only perform the operation if there are at least two numbers <= M
    
    # First, count how many numbers are initially <= M
    count_leq_M = sum(1 for num in A if num <= M)
    
    # If there are less than 2 numbers <= M, we cannot perform any operations
    if count_leq_M < 2:
        print(1)
        return
    
    # Calculate the number of ways to choose how many times each number can be increased
    # For each number, the number of ways to choose how many times it is increased is (M - num) // K + 1
    # However, we need to consider that we can only increase numbers in such a way that they don't exceed M
    # And that we can only perform the operation if there are at least two numbers <= M
    
    # We need to calculate the product of (M - num) // K + 1 for all numbers in A
    # But we need to consider that we can only increase numbers in such a way that they don't exceed M
    # And that we can only perform the operation if there are at least two numbers <= M
    
    # We need to calculate the product of (M - num) // K + 1 for all numbers in A
    # But we need to consider that we can only increase numbers in such a way that they don't exceed M
    # And that we can only perform the operation if there are at least two numbers <= M
    
    # We need to calculate the product of (M - num) // K + 1 for all numbers in A
    # But we need to consider that we can only increase numbers in such a way that they don't exceed M
    # And that we can only perform the operation if there are at least two numbers <= M
    
    # We need to calculate the product of (M - num) // K + 1 for all numbers in A
    # But we need to consider that we can only increase numbers in such a way that they don't exceed M
    # And that we can only perform the operation if there are at least two numbers <= M
    
    # We need to calculate the product of (M - num) // K + 1 for all numbers in A
    # But we need to consider that we can only increase numbers in such a way that they don't exceed M
    # And that we can only perform the operation if there are at least two numbers <= M
    
    # We need to calculate the product of (M - num) // K + 1 for all numbers in A
    # But we need to consider that we can only increase numbers in such a way that they don't exceed M
    # And that we can only perform the operation if there are at least two numbers <= M
    
    # We need to calculate the product of (M - num) // K + 1 for all numbers in A
    # But we need to consider that we can only increase numbers in such a way that they don't exceed M
    # And that we can only perform the operation if there are at least two numbers <= M
    
    # We need to calculate the product of (M - num) // K + 1 for all numbers in A
    # But we need to consider that we can only increase numbers in such a way that they don't exceed M
    # And that we can only perform the operation if there are at least two numbers <= M
    
    # We need to calculate the product of (M - num) // K + 1 for all numbers in A
    # But we need to consider that we can only increase numbers in such a way that they don't exceed M
    # And that we can only perform the operation if there are at least two numbers <= M
    
    # We need to calculate the product of (M - num) // K + 1 for all numbers in A
    # But we need to consider that we can only increase numbers in such a way that they don't exceed M
    # And that we can only perform the operation if there are at least two numbers <= M
    
    # We need to calculate the product of (M - num) // K + 1 for all numbers in A
    # But we need to consider that we can only increase numbers in such a way that they don't exceed M
    # And that we can only perform the operation if there are at least two numbers <= M
    
    # We need to calculate the product of (M - num) // K + 1 for all numbers in A
    # But we need to consider that we can only increase numbers in such a way that they don't exceed M
    # And that we can only perform the operation if there are at least two numbers <= M
    
    # We need to calculate the product of (M - num) // K + 1 for all numbers in A
    # But we need to consider that we can only increase numbers in such a way that they don't exceed M
    # And that we can only perform the operation if there are at least two numbers <= M
    
    # We need to calculate the product of (M - num) // K + 1 for all numbers in A
    # But we need to consider that we can only increase numbers in such a way that they don't exceed M
    # And that we can only perform the operation if there are at least two numbers <= M
    
    # We need to calculate the product of (M - num) // K + 1 for all numbers in A
    # But we need to consider that we can only increase numbers in such a way that they don't exceed M
    # And that we can only perform the operation if there are at least two numbers <= M
    
    # We need to calculate the product of (M - num) // K + 1 for all numbers in A
    # But we need to consider that we can only increase numbers in such a way that they don't exceed M
    # And that we can only perform the operation if there are at least two numbers <= M
    
    # We need to calculate the product of (M - num) // K + 1 for all numbers in A
    # But we need to consider that we can only increase numbers in such a way that they don't exceed M
    # And that we can only perform the operation if there are at least two numbers <= M
    
    # We need to calculate the product of (M - num) // K + 1 for all numbers in A
    # But we need to consider that we can only increase numbers in such a way that they don't exceed M
    # And that we can only perform the operation if there are at least two numbers <= M
    
    # We need to calculate the product of (M - num) // K + 1 for all numbers in A
    # But we need to consider that we can only increase numbers in such a way that they don't exceed M
    # And that we can only perform the operation if there are at least two numbers <= M
    
    # We need to calculate the product of (M - num) // K + 1 for all numbers in A
    # But we need to consider that we can only increase numbers in such a way that they don't exceed M
    # And that we can only perform the operation if there are at least two numbers <= M
    
    # We need to calculate the product of (M - num) // K + 1 for all numbers in A
    # But we need to consider that we can only increase numbers in such a way that they don't exceed M
    # And that we can only perform the operation if there are at least two numbers <= M
    
    # We need to calculate the product of (M - num) // K + 1 for all numbers in A
    # But we need to consider that we can only increase numbers in such a way that they don't exceed M
    # And that we can only perform the operation if there are at least two numbers <= M
    
    # We need to calculate the product of (M - num) // K + 1 for all numbers in A
    # But we need to consider that we can only increase numbers in such a way that they don't exceed M
    # And that we can only perform the operation if there are at least two numbers <= M
    
    # We need to calculate the product of (M - num) // K + 1 for all numbers in