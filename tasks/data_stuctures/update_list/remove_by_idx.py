class Node:
    def __init__(self, value, next_item=None) -> None:
        self.value = value
        self.next_item = next_item


def solution(node: Node, idx: int) -> Node:
    """
    Удаляет элемент из односвязного списка по индексу (0-based).
    Возвращает голову обновленного списка.
    """
    if idx == 0:
        return node.next_item

    current = node
    for _ in range(idx - 1):
        if current.next_item is None:
            return node
        current = current.next_item

    if current.next_item is not None:
        current.next_item = current.next_item.next_item

    return node
