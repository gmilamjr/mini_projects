"""
Script to determine all prime numbers within a specified range

A performance comparison is done with a sortedset vs set
"""
from sortedcontainers import SortedSet
from timeit import default_timer as timer

def primes_finder(n):
    
    #number range to be checked
    number_range = set(range(2, n+1))
    
    #empty list to append discovered primes to
    primes_list = []
    
    while number_range:
        prime = number_range.pop()
        primes_list.append(prime)
        multiples = set(range(prime*2, n+1, prime))
        number_range.difference_update(multiples)
    
    # NUmber of primes that were found
    prime_count = len(primes_list)
    
    #largest prime
    largest_prime = max(primes_list)
    
    #Summary
    print(f"There are {prime_count} prime numbers between 2 and {n}, the largest of which is {largest_prime}")
    return primes_list

def primes_finder_sorted(n):
    
    #number range to be checked
    number_range = SortedSet(range(2, n+1))
    
    #empty list to append discovered primes to
    primes_list = []
    
    while number_range:
        prime = number_range.pop(0)
        primes_list.append(prime)
        multiples = set(range(prime*2, n+1, prime))
        number_range.difference_update(multiples)
    
    # NUmber of primes that were found
    prime_count = len(primes_list)
    
    #largest prime
    largest_prime = max(primes_list)
    
    #Summary
    print(f"There are {prime_count} prime numbers between 2 and {n}, the largest of which is {largest_prime}")
    return primes_list


