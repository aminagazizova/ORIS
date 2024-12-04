import threading

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(start, end, thread_id, result):
    primes_in_range = []
    for num in range(start, end):
        if is_prime(num):
            primes_in_range.append(num)
    result[thread_id] = primes_in_range

if __name__ == "__main__":
    range_start = 10
    range_end = 100
    num_threads = 4
    thread_ranges = []
    result = [None] * num_threads

    step = (range_end - range_start) // num_threads
    for i in range(num_threads):
        start = range_start + i * step
        end = range_start + (i + 1) * step if i != num_threads - 1 else range_end
        thread_ranges.append((start, end))

    threads = []
    for i in range(num_threads):
        start, end = thread_ranges[i]
        thread = threading.Thread(target=find_primes, args=(start, end, i, result))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    all_primes = []
    for primes in result:
        if primes is not None:
            all_primes.extend(primes)

    print(f"Простые числа в диапазоне от {range_start} до {range_end}: {all_primes}")
