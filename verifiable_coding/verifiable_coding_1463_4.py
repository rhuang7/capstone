import sys
import math
from collections import defaultdict

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    
    def get_prime_factors(n):
        factors = {}
        while n % 2 == 0:
            factors[2] = True
            n //= 2
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors[i] = True
                n //= i
            i += 2
        if n > 1:
            factors[n] = True
        return factors
    
    def get_prime_factors_list(n):
        factors = []
        while n % 2 == 0:
            factors.append(2)
            n //= 2
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors.append(i)
                n //= i
            i += 2
        if n > 1:
            factors.append(n)
        return factors
    
    def get_prime_factors_set(n):
        factors = set()
        while n % 2 == 0:
            factors.add(2)
            n //= 2
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors.add(i)
                n //= i
            i += 2
        if n > 1:
            factors.add(n)
        return factors
    
    def get_prime_factors_dict(n):
        factors = {}
        while n % 2 == 0:
            factors[2] = True
            n //= 2
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors[i] = True
                n //= i
            i += 2
        if n > 1:
            factors[n] = True
        return factors
    
    def get_prime_factors_list_with_count(n):
        factors = []
        while n % 2 == 0:
            factors.append(2)
            n //= 2
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors.append(i)
                n //= i
            i += 2
        if n > 1:
            factors.append(n)
        return factors
    
    def get_prime_factors_set_with_count(n):
        factors = set()
        while n % 2 == 0:
            factors.add(2)
            n //= 2
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors.add(i)
                n //= i
            i += 2
        if n > 1:
            factors.add(n)
        return factors
    
    def get_prime_factors_dict_with_count(n):
        factors = {}
        while n % 2 == 0:
            factors[2] = True
            n //= 2
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors[i] = True
                n //= i
            i += 2
        if n > 1:
            factors[n] = True
        return factors
    
    def get_prime_factors_list_with_count_and_unique(n):
        factors = []
        while n % 2 == 0:
            factors.append(2)
            n //= 2
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors.append(i)
                n //= i
            i += 2
        if n > 1:
            factors.append(n)
        return factors
    
    def get_prime_factors_set_with_count_and_unique(n):
        factors = set()
        while n % 2 == 0:
            factors.add(2)
            n //= 2
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors.add(i)
                n //= i
            i += 2
        if n > 1:
            factors.add(n)
        return factors
    
    def get_prime_factors_dict_with_count_and_unique(n):
        factors = {}
        while n % 2 == 0:
            factors[2] = True
            n //= 2
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors[i] = True
                n //= i
            i += 2
        if n > 1:
            factors[n] = True
        return factors
    
    def get_prime_factors_list_with_count_and_unique_and_sorted(n):
        factors = []
        while n % 2 == 0:
            factors.append(2)
            n //= 2
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors.append(i)
                n //= i
            i += 2
        if n > 1:
            factors.append(n)
        return factors
    
    def get_prime_factors_set_with_count_and_unique_and_sorted(n):
        factors = set()
        while n % 2 == 0:
            factors.add(2)
            n //= 2
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors.add(i)
                n //= i
            i += 2
        if n > 1:
            factors.add(n)
        return factors
    
    def get_prime_factors_dict_with_count_and_unique_and_sorted(n):
        factors = {}
        while n % 2 == 0:
            factors[2] = True
            n //= 2
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors[i] = True
                n //= i
            i += 2
        if n > 1:
            factors[n] = True
        return factors
    
    def get_prime_factors_list_with_count_and_unique_and_sorted_and_unique(n):
        factors = []
        while n % 2 == 0:
            factors.append(2)
            n //= 2
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors.append(i)
                n //= i
            i += 2
        if n > 1:
            factors.append(n)
        return factors
    
    def get_prime_factors_set_with_count_and_unique_and_sorted_and_unique(n):
        factors = set()
        while n % 2 == 0:
            factors.add(2)
            n //= 2
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors.add(i)
                n //= i
            i += 2
        if n > 1:
            factors.add(n)
        return factors
    
    def get_prime_factors_dict_with_count_and_unique_and_sorted_and_unique(n):
        factors = {}
        while n % 2 == 0:
            factors[2] = True
            n //= 2
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors[i] = True
                n //= i
            i += 2
        if n > 1:
            factors[n] = True
        return factors
    
    def get_prime_factors_list_with_count_and_unique_and_sorted_and_unique_and_sorted(n):
        factors = []
        while n % 2 == 0:
            factors.append(2)
            n //= 2
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors.append(i)
                n //= i
            i += 2
        if n > 1:
            factors.append(n)
        return factors
    
    def get_prime_factors_set_with_count_and_unique_and_sorted_and_unique_and_sorted(n):
        factors = set()
        while n % 2 == 0:
            factors.add(2)
            n //= 2
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors.add(i)
                n //= i
            i += 2
        if n > 1:
            factors.add(n)
        return factors
    
    def get_prime_factors_dict_with_count_and_unique_and_sorted_and_unique_and_sorted(n):
        factors = {}
        while n % 2 == 0:
            factors[2] = True
            n //= 2
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors[i] = True
                n //= i
            i += 2
        if n > 1:
            factors[n] = True
        return factors
    
    def get_prime_factors_list_with_count_and_unique_and_sorted_and_unique_and_sorted_and_unique(n):
        factors = []
        while n % 2 == 0:
            factors.append(2)
            n //= 2
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors.append(i)
                n //= i
            i += 2
        if n > 1:
            factors.append(n)
        return factors
    
    def get_prime_factors_set_with_count_and_unique_and_sorted_and_unique_and