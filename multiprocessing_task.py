import multiprocessing
import requests
import time
import cProfile

prime_pos = []

def is_primes(n):
    global prime_pos
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    for numbers in range(2, int(n**0.5)+1):
        if primes[numbers]:
            for mult in range(numbers*numbers, n+1, numbers):
                primes[mult] = False
    prime_pos = primes

def find_primes(chunk):
    for x in chunk:
        print(x)
        input()

    
    

def find_primes_in_range(numbers):
    maxs = max(numbers)
    is_primes(maxs)
    chunksize = len(numbers)//multiprocessing.cpu_count()
    chunks  = [numbers[i:i+chunksize] for i in range(0, len(numbers), chunksize)]
    print(len(prime_pos),maxs)
    input()
    with multiprocessing.Pool() as pool:
        results = pool.map(find_primes, chunks)
        return results
