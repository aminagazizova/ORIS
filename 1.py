import threading
import time

def thread_function(name):
    print(f"Поток {name} стартует.")
    time.sleep(2)
    print(f"Поток {name} завершен.")

if __name__ == "__main__":
    num_threads = 5
    threads = []

    for i in range(num_threads):
        thread_name = f"Name-{i+1}"
        thread = threading.Thread(target=thread_function, args=(thread_name,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Все потоки завершили свою работу.")
