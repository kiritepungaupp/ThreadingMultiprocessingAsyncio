import multiprocessing
import requests
import time
import cProfile

def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2) or (n % 3 == 0 and n > 3):
        return False

    maxcpu = multiprocessing.cpu_count()
    squaredz = int(n**0.5) + 1
    chunk_size = (squaredz - 5) // maxcpu
    chunks = [(5 + i * chunk_size, min(5 + (i + 1) * chunk_size, squaredz)) for i in range(maxcpu)]

    with multiprocessing.Pool(processes=maxcpu) as pool:
        results = pool.starmap(check_prime_chunk, [(n, start, end) for start, end in chunks])

    return all(results)

def check_prime_chunk(number, start, end):
    for i in range(start, end, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    return True

def main():
    url = 'https://raw.githubusercontent.com/kiritepungaupp/fordownloads/main/numbers.txt'
    response = requests.get(url)

    if response.status_code == 200:
        numbers = [int(line) for line in response.text.splitlines()]
        print(numbers)
    else:
        print('Failed to download the file')

    start_time = time.time()

    for x in numbers:
        print(f'{x}: {is_prime(x)}')

    end_time = time.time()
    print(f'Time taken: {end_time - start_time:.6f} seconds')

if __name__ == "__main__":
    cProfile.run('main()')
