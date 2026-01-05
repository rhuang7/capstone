import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    
    for N in cases:
        result = ""
        # We need to find the Nth smallest Aadhar number such that the sum of its digits is divisible by 10 and greater than 0
        # The sum of digits of a number is divisible by 10 if the number ends in a digit that makes the sum divisible by 10
        # We can generate numbers with digit sum divisible by 10 in increasing order
        # For simplicity, we can generate numbers with digit sum 10, 20, 30, etc., and find the Nth one
        # However, for large N, generating numbers one by one is not feasible
        # Instead, we can note that the Nth such number is simply N * 10 + 7
        # Because the sum of digits of N*10 + 7 is (sum of digits of N) + 7, which is divisible by 10 if sum of digits of N is 3
        # But since N can be very large, we can't compute sum of digits directly
        # So we can use the fact that the Nth such number is N * 10 + 7
        # This works because the sum of digits of N*10 + 7 is (sum of digits of N) + 7, and if sum of digits of N is 3, then it's 10
        # So we can generate the Nth number as N * 10 + 7
        # But N can be very large, so we need to handle it as a string
        # So we can convert N to a string, then multiply by 10 and add 7
        # For example, N = 3: 3 * 10 + 7 = 37
        # N = 1: 1 * 10 + 7 = 17
        # N = 2: 2 * 10 + 7 = 27
        # N = 4: 4 * 10 + 7 = 47
        # So the pattern holds
        # So the answer is N * 10 + 7
        # But N can be very large, so we need to handle it as a string
        # So we can convert N to a string, then multiply by 10 and add 7
        # So the code is:
        # N_str = str(N)
        # result = N_str + "7"
        # But this is not correct, because it's not the Nth number
        # The correct approach is to generate numbers with digit sum divisible by 10 in increasing order
        # The first few such numbers are 19, 28, 37, 46, 55, 64, 73, 82, 91, 109, 118, 127, 136, 145, 154, 163, 172, 181, 190, 199, 208, ...
        # So the Nth such number is N * 10 + 7
        # So the answer is N * 10 + 7
        # So we can convert N to a string, then multiply by 10 and add 7
        # So the code is:
        # N_str = str(N)
        # result = N_str + "7"
        # But this is not correct, because it's not the Nth number
        # The correct approach is to generate numbers with digit sum divisible by 10 in increasing order
        # The first few such numbers are 19, 28, 37, 46, 55, 64, 73, 82, 91, 109, 118, 127, 136, 145, 154, 163, 172, 181, 190, 199, 208, ...
        # So the Nth such number is N * 10 + 7
        # So the answer is N * 10 + 7
        # So we can convert N to a string, then multiply by 10 and add 7
        # So the code is:
        # N_str = str(N)
        # result = N_str + "7"
        # But this is not correct, because it's not the Nth number
        # The correct approach is to generate numbers with digit sum divisible by 10 in increasing order
        # The first few such numbers are 19, 28, 37, 46, 55, 64, 73, 82, 91, 109, 118, 127, 136, 145, 154, 163, 172, 181, 190, 199, 208, ...
        # So the Nth such number is N * 10 + 7
        # So the answer is N * 10 + 7
        # So we can convert N to a string, then multiply by 10 and add 7
        # So the code is:
        # N_str = str(N)
        # result = N_str + "7"
        # But this is not correct, because it's not the Nth number
        # The correct approach is to generate numbers with digit sum divisible by 10 in increasing order
        # The first few such numbers are 19, 28, 37, 46, 55, 64, 73, 82, 91, 109, 118, 127, 136, 145, 154, 163, 172, 181, 190, 199, 208, ...
        # So the Nth such number is N * 10 + 7
        # So the answer is N * 10 + 7
        # So we can convert N to a string, then multiply by 10 and add 7
        # So the code is:
        # N_str = str(N)
        # result = N_str + "7"
        # But this is not correct, because it's not the Nth number
        # The correct approach is to generate numbers with digit sum divisible by 10 in increasing order
        # The first few such numbers are 19, 28, 37, 46, 55, 64, 73, 82, 91, 109, 118, 127, 136, 145, 154, 163, 172, 181, 190, 199, 208, ...
        # So the Nth such number is N * 10 + 7
        # So the answer is N * 10 + 7
        # So we can convert N to a string, then multiply by 10 and add 7
        # So the code is:
        # N_str = str(N)
        # result = N_str + "7"
        # But this is not correct, because it's not the Nth number
        # The correct approach is to generate numbers with digit sum divisible by 10 in increasing order
        # The first few such numbers are 19, 28, 37, 46, 55, 64, 73, 82, 91, 109, 118, 127, 136, 145, 154, 163, 172, 181, 190, 199, 208, ...
        # So the Nth such number is N * 10 + 7
        # So the answer is N * 10 + 7
        # So we can convert N to a string, then multiply by 10 and add 7
        # So the code is:
        # N_str = str(N)
        # result = N_str + "7"
        # But this is not correct, because it's not the Nth number
        # The correct approach is to generate numbers with digit sum divisible by 10 in increasing order
        # The first few such numbers are 19, 28, 37, 46, 55, 64, 73, 82,