import threading


#сортировка массива
def sort_subarray(subarray):
    subarray.sort()


#объединяем
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    #добавляем остаток
    result.extend(left[i:])
    result.extend(right[j:])

    return result


if __name__ == "__main__":
    import random
    import time

    #генерируем большой массив
    array_size = 100000  # Размер массива
    random_array = [random.randint(0, 1000000) for _ in range(array_size)]

    num_threads = int(input("Введите количество потоков: "))

    #разделяем на подмассивы
    step = len(random_array) // num_threads
    threads = []
    sorted_subarrays = []

    #потоки для подмассивов
    for i in range(num_threads):
        start = i * step

        end = len(random_array) if i == num_threads - 1 else start + step
        subarray = random_array[start:end]
        thread = threading.Thread(target=sort_subarray, args=(subarray,))

        threads.append(thread)
        sorted_subarrays.append(subarray)
        thread.start()

    #завершаем все потоки
    for thread in threads:
        thread.join()

    # объединяем потоки
    sorted_array = sorted_subarrays[0]
    for i in range(1, len(sorted_subarrays)):
        sorted_array = merge(sorted_array, sorted_subarrays[i])

    print("Отсортированный массив:", sorted_array[:10])
