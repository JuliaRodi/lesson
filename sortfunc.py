# Практика часть 1

# Пузырьковый алгоритм сортировки. Пузырьковая сортировка работает следующим образом: сначала берутся первые два
# элемента массива и сравниваются между собой. Если первый элемент больше второго
# (или меньше, в зависимости от условий), они меняются местами. Затем алгоритм продолжает сравнивать и
# менять местами следующие пары элементов. Однако одного прохода по списку недостаточно, чтобы убедиться,
# что массив полностью отсортирован, поэтому требуется несколько таких проходов.

# nums = [5, 6, 2, 1, 3, 4]
#
# def buble_sort(ls):
#     swapped = True
#     while swapped:
#         swapped = False
#         for i in range(len(ls) - 1):
#             if ls[i] > ls[i + 1]:
#                 ls[i], ls[i + 1] = ls[i + 1], ls[i]
#                 swapped = True
#
# buble_sort(nums)
# print(nums)
#
# # Сортировка выборкой. Принцип работы этого алгоритма основан на разделении списка на две части:
# # отсортированную и неотсортированную. Мы будем перебирать все элементы в неотсортированной части и
# # находить минимальный элемент, который затем переместим в отсортированную часть списка.
#
# def selection_sort(ls):
#     for i in range(len(ls)):
#         lowest = i
#         for j in range(i+1, len(ls)):
#             if ls[j] < ls[lowest]:
#                 lowest = j
#         ls[i], ls[lowest] = ls[lowest], ls[i]
#
# selection_sort(nums)
# print(nums)

# Практика часть 2

# На этом занятии продолжаем работать с нашим пакетом. По итогу добавили ещё 1 алгоритм сортировки,
# чтобы у нас файл не был слишком пустым. Получилось нечто, напоминающее модуль, содержащий в себе
# несколько функций, которые могут использовать ваши коллеги

import time

tic = time.perf_counter()
def buble_sort(ls):
    for i in range(len(ls) - 1, 0, -1):
        for j in range(i):
            if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
    return ls
toc = time.perf_counter()
print(f"Пузырьковая сортировка заняла {toc - tic:f} секунд")

tic = time.perf_counter()
def selection_sort(ls):
    for i in range(len(ls) - 1):
        min_index = i
        for j in range(i + 1, len(ls)):
            if ls[min_index] > ls[j]:
                min_index = j
                ls[min_index], ls[j] = ls[j], ls[min_index]
    return ls
toc = time.perf_counter()
print(f"Сортировка выборкой заняла {toc - tic:f} секунд")

#Сортировка вставками - это алгоритм сортировки, в котором элементы входной последовательности
# просматриваются по одному, и каждый новый поступивший элемент размещается в подходящее место среди
# ранее упорядоченных элементов

tic = time.perf_counter()
def insertion_sort(ls):
    for i in range(1, len(ls)):
        key = ls[i]
        j = i - 1
        while ls[j] > key and j >= 0:
            ls[j + 1] = ls[j]
            j -= 1
            ls[j + 1] = key
    return ls
toc = time.perf_counter()
print(f"Сортировка вставками заняла {toc - tic:f} секунд")
