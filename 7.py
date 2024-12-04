import threading
from collections import defaultdict


def word_count(text_chunk, result_dict):
    local_count = defaultdict(int)
    words = text_chunk.split()

    for word in words:
        word = word.lower()
        local_count[word] += 1

    with threading.Lock():
        for word, count in local_count.items():
            result_dict[word] += count


def split_text(text, num_chunks):
    avg_chunk_size = len(text) // num_chunks
    chunks = [text[i:i + avg_chunk_size] for i in range(0, len(text), avg_chunk_size)]
    return chunks


def main(text, num_threads):
    result_dict = defaultdict(int)
    chunks = split_text(text, num_threads)

    threads = []
    for chunk in chunks:
        thread = threading.Thread(target=word_count, args=(chunk, result_dict))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    for word, count in sorted(result_dict.items()):
        print(f"{word}: {count}")


if __name__ == "__main__":
    text = """Напишите программу, которая разбивает текстовый файл на
равные части и использует потоки для параллельного подсчета частоты каждого слова. В конце нужно объединить результаты из всех потоков и вывести итоговую статистику."""

    num_threads = 4
    main(text, num_threads)
