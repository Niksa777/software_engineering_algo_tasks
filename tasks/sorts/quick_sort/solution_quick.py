def quick_sort(arr: list[int]) -> list[int]:
    """
    Быстрая сортировка массива целых чисел по возрастанию.
    Возвращает новый отсортированный массив, исходный не изменяется.
    """
    if not arr:
        return []
    result = arr[:]  # копия – исходный массив остаётся нетронутым
    _quicksort(result, 0, len(result) - 1)
    print(result)

    return result


def _quicksort(arr: list[int], low: int, high: int) -> None:
    """Рекурсивная in-place сортировка подмассива arr[low..high]."""
    while low < high:
        # --- выбор опорного элемента: медиана трёх (low, mid, high) ---
        mid = (low + high) // 2
        if arr[mid] < arr[low]:
            arr[low], arr[mid] = arr[mid], arr[low]
        if arr[high] < arr[low]:
            arr[low], arr[high] = arr[high], arr[low]
        if arr[high] < arr[mid]:
            arr[mid], arr[high] = arr[high], arr[mid]

        pivot = arr[mid]
        arr[mid], arr[high] = arr[high], arr[mid]

        # --- разбиение Ломуто ---
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        i += 1
        arr[i], arr[high] = arr[high], arr[i]
        p = i  # итоговая позиция опорного элемента

        # --- хвостовая оптимизация: рекурсивно обрабатываем меньшую часть ---
        if p - low < high - p:
            _quicksort(arr, low, p - 1)
            low = p + 1
        else:
            _quicksort(arr, p + 1, high)
            high = p - 1


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    if 0 <= len(arr) <= 10**5:
        quick_sort(arr)
    else:
        print("Неверный ввод. Количество заявленных элементов не соответствует требованиям")
