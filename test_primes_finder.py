# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 16:16:05 2022
@author: Gary Milam Jr

Test script of primes finder.
"""

import pytest
from primes_finder import primes_finder, primes_finder_sorted

def test_get_correct_primes():
    n = 100
    gt_pl = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
    
    pl = set(primes_finder(n))
    
    assert gt_pl == pl
    
def test_get_correct_primes_sortedset():
    n = 100
    gt_pl = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
    
    pl = set(primes_finder_sorted(n))
    
    assert gt_pl == pl

def test_speed_primes():
    from timeit import default_timer as timer
    n = 10000000
    start =  timer()
    primes_finder(n)
    end = timer()
    
    exec_time = end-start
    print(f"Time for non sorted set {exec_time}")
    assert exec_time < 10

def test_speed_primes_sortedset():
    from timeit import default_timer as timer
    n = 10000000
    start =  timer()
    primes_finder_sorted(n)
    end = timer()
    exec_time = end-start
    
    print(f"Time for sorted set {exec_time}")
    assert exec_time < 100