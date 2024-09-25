import math
import requests
import time

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check for factors from 5 to sqrt(n), skipping even numbers
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
            
    return True

# Example usage
if __name__ == "__main__":
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

# Print results

  print(f"Time taken: {end_time - start_time:.6f} seconds")
