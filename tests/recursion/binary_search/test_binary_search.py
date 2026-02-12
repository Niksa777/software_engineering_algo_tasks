from tasks.recursion.binary_search.solution_binary import binary_search


def test_binary_search() -> None:
    """Тесты для проверки корректности и граничных случаев."""

    # Тест 1: Найден элемент (дубликаты)
    arr = [1, 2, 2, 4, 7]
    assert binary_search(arr, 2) in (1, 2)  # Любой из индексов 1 или 2

    # Тест 2: Элемент отсутствует
    arr = [1, 3, 5]
    assert binary_search(arr, 2) == -1

    # Тест 3: Пустой массив
    assert binary_search([], 10) == -1

    # Тест 4: Один элемент (найден)
    assert binary_search([42], 42) == 0

    # Тест 5: Один элемент (не найден)
    assert binary_search([42], 0) == -1

    # Тест 6: Большой массив (10^6 элементов)
    import random

    large_arr = sorted([random.randint(-(10**9), 10**9) for _ in range(10**6)])
    target = large_arr[500000]  # гарантированно есть
    assert binary_search(large_arr, target) == 500000

    # Тест 7: Элемент в начале
    assert binary_search([1, 2, 3], 1) == 0

    # Тест 8: Элемент в конце
    assert binary_search([1, 2, 3], 3) == 2

    # Тест 9: Минимальные отрицательные значения
    assert binary_search([-(10**9), -5, 0], -(10**9)) == 0

    # Тест 10: Максимальные значения
    assert binary_search([0, 5, 10**9], 10**9) == 2


if __name__ == "__main__":
    test_binary_search()
