import asyncio

async def async_save_to_disk(file_name, content):
    with open(file_name, 'w') as file_handle:
        for line in content:
            formatted_line = f"{str(line)}\n"
            file_handle.write(formatted_line)

async def run_async_tasks(prime_numbers):
    file_names = ['primes_1.txt', 'primes_2.txt', 'primes_3.txt', 'primes_4.txt', 
                  'primes_5.txt', 'primes_6.txt', 'primes_7.txt', 'primes_8.txt', 
                  'primes_9.txt', 'primes_10.txt']

    segmented_data = [prime_numbers[i::len(file_names)] for i in range(len(file_names))]
    
    tasks = []
    for index in range(len(file_names)):
        task = async_save_to_disk(file_names[index], segmented_data[index])
        tasks.append(task)

    await asyncio.gather(*tasks)


