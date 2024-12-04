import threading

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def compute_fibonacci(start, end, thread_id, results):
    thread_results = []
    for i in range(start, end):
        thread_results.append((i, fibonacci(i)))
    results[thread_id] = thread_results

if __name__ == "__main__":
    n = int(input("Введите до какого числа Фибоначчи нужно вычислить: "))
    num_threads = int(input("Введите количество потоков: "))

    results = [None] * num_threads
    threads = []

    step = (n // num_threads) + (1 if n % num_threads != 0 else 0)

    for i in range(num_threads):
        start = i * step
        end = min(start + step, n + 1)
        if start < n + 1:
            thread = threading.Thread(target=compute_fibonacci, args=(start, end, i, results))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    final_results = []
    for thread_result in results:
        if thread_result is not None:
            final_results.extend(thread_result)

    print("Результаты вычислений чисел Фибоначчи:")
    for number, fib_value in final_results:
        print(f"F({number}) = {fib_value}")
