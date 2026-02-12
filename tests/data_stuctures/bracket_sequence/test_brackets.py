from tasks.data_stuctures.bracket_sequence.brackets import is_correct_bracket_seq


def test_brackets() -> None:
    """Тесты для проверки скобочной последовательности."""

    # Тест 1: Корректная вложенность
    assert is_correct_bracket_seq("{[()]})") is True

    # Тест 2: Простые скобки
    assert is_correct_bracket_seq("()") is True

    # Тест 3: Пустая строка
    assert is_correct_bracket_seq("") is True

    # Тест 4: Неправильный порядок
    assert is_correct_bracket_seq("([)]") is False

    # Тест 5: Лишняя закрывающая
    assert is_correct_bracket_seq("()(") is False

    # Тест 6: Лишняя открывающая
    assert is_correct_bracket_seq("(()") is False

    # Тест 7: Только одна пара
    assert is_correct_bracket_seq("{}") is True

    # Тест 8: Смешанные типы
    assert is_correct_bracket_seq("([]{})") is True


if __name__ == "__main__":
    test_brackets()
