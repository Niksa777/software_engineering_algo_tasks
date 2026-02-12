def binary_search(arr: list[int], target: int) -> int:
    """
    Бинарный поиск в отсортированном массиве.
    Возвращает индекс target или -1, если не найден.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            print(mid)
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    print("-1")
    return -1
