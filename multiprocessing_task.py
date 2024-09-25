import multiprocessing
import time



def is_primes(n):
    global prime_pos
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    for numbers in range(2, int(n**0.5)+1):
        if primes[numbers]:
            for mult in range(numbers*numbers, n+1, numbers):
                primes[mult] = False
    return primes

def find_primes(chunk, prime_pos):
    return [x for x in chunk if prime_pos[x]]
    
    

def find_primes_in_range(numbers):
    maxs = max(numbers)
    prime_pos = is_primes(maxs)
    chunksize = len(numbers)//multiprocessing.cpu_count()
    chunks  = [numbers[i:i+chunksize] for i in range(0, len(numbers), chunksize)]
    with multiprocessing.Pool() as pool:
        results = pool.starmap(find_primes,[ (chunk, prime_pos) for chunk in chunks])
        return [prime for sublist in results for prime in sublist]