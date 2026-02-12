import io
import sys

from tasks.data_stuctures.tasks_list.print_list import Node, solution


def capture_output(func, *args):
    buffer = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = buffer
    try:
        func(*args)
    finally:
        sys.stdout = old_stdout
    return buffer.getvalue()


def test_print_list() -> None:
    """Тесты для проверки корректности печати списка."""
    # Тест 1: Один элемент
    node1 = Node(42)
    expected = ["42"]
    assert capture_output(solution, node1) == expected

    # Тест 2: Пример из ТЗ
    node3 = Node("node3")
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    expected = ["node0", "node1", "node2", "node3"]
    assert capture_output(solution, node0) == expected

    # Тест 3: Большой список (5000 элементов)
    head = Node(0)
    cur = head
    for i in range(1, 100):
        cur.next_item = Node(i)
        cur = cur.next_item

    out = capture_output(solution, head)
    assert out.startswith("0\n1\n2\n")
    assert out.endswith("97\n98\n99\n")

    # Тест 4: Список с числами и строками
    nodeC = Node("Charlie")
    nodeB = Node(123)
    nodeA = Node(True)
    nodeA.next_item = nodeB
    nodeB.next_item = nodeC
    expected = ["True", "123", "Charlie"]
    assert capture_output(solution, nodeA) == expected

    # Тест 5: Только числа
    node3 = Node(-100)
    node2 = Node(0)
    node1 = Node(3.14)
    node0 = Node(42)
    node0.next_item = node1
    node1.next_item = node2
    node2.next_item = node3
    expected = ["42", "3.14", "0", "-100"]
    assert capture_output(solution, node0) == expected


if __name__ == "__main__":
    test_print_list()
