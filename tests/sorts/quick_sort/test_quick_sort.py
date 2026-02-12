import random

from tasks.sorts.quick_sort.solution_quick import quick_sort


def test_quick_sort() -> None:
    """Набор тестов для проверки корректности и производительности."""

    # Тесты: Граничные случаи
    assert quick_sort([]) == []
    assert quick_sort([3]) == [3]
    assert quick_sort([7, 7, 7, 7]) == [7, 7, 7, 7]

    # Тест: Массив из примера
    assert quick_sort([3, 7, 9, 4, 3, 1, 8, 5]) == [1, 3, 3, 4, 5, 7, 8, 9]

    # Тест: Упорядоченный массив
    assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Тест: Массив в обратном порядке
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    # Тест: Отрицательные числа и дубликаты
    assert quick_sort([2, -1, 2, -1, 0]) == [-1, -1, 0, 2, 2]

    # Тест: Случайный массив (проверка на 1000 элементов)
    arr_random = [random.randint(-(10**6), 10**6) for _ in range(1000)]
    assert quick_sort(arr_random) == sorted(arr_random)
