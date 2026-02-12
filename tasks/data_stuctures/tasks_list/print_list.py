class Node:
    def __init__(self, value, next_item=None) -> None:
        self.value = value
        self.next_item = next_item


def solution(node: Node) -> None:
    """
    Печатает все элементы односвязного списка, каждый на новой строке.
    O(n) время, O(1) память.
    """
    current = node
    while current:
        print(current.value)
        current = current.next_item
