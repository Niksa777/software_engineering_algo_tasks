def bubble_sort(arr: list[int]) -> list[list[int]]:
    """Сортировка пузырьком с выводом только после проходов с обменами."""
    snapshots = []
    n = len(arr)
    arr = arr.copy()
    has_swaps = False  # флаг для вывода при изначально отсортированном массиве
    if 1 < n < 1001:
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
                    has_swaps = True

            # Если обмен произошел, выводим обновленный массив
            if swapped:
                snapshots.append(arr.copy())
                print(" ".join(map(str, arr)))

        # Если ни одного обмена не было — выводим исходный массив
        if not has_swaps:
            snapshots.append(arr.copy())
            print(" ".join(map(str, arr)))

    else:
        print(
            "Размер массива не удовлетворяет заданным ограничениям. "
            "Длина массива должна быть в отрезке от 2 до 1000 эл."
        )
    return snapshots


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    if n == len(arr):
        bubble_sort(arr)
    else:
        print(
            "Неверный ввод. Количество заявленных элементов "
            "не совпадает с настоящей длиной массива"
        )
