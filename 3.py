import threading
import math

def partial_factorial(start, end, thread_id, result):
    product = 1
    for i in range(start, end):
        product *= i
    result[thread_id] = product

if __name__ == "__main__":
    number = 10
    num_threads = 4
    result = [None] * num_threads

    step = number // num_threads
    threads = []

    for i in range(num_threads):
        start = i * step + 1
        end = (i + 1) * step + 1 if i != num_threads - 1 else number + 1
        thread = threading.Thread(target=partial_factorial, args=(start, end, i, result))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    final_result = 1
    for partial in result:
        if partial is not None:
            final_result *= partial

    print(f"Факториал {number} = {final_result}")
