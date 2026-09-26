# tests/test_validator.py
from validator import validate_email, validate_phone, validate_snils


def test_validate_email():
    assert validate_email("test@example.com") is True
    assert validate_email("invalid") is False


def test_validate_phone_valid():
    assert validate_phone("+79161234567") is True
    assert validate_phone("89161234567") is True


def test_validate_phone_invalid():
    assert validate_phone("12345") is False
    assert validate_phone("+7916123456") is False  # 10 цифр
    assert validate_phone("+99161234567") is False  # первая не 7/8


def test_validate_snils():
    # Валидные СНИЛС (рассчитаны по алгоритму)
    assert validate_snils("11223344595") is True
    assert validate_snils("001-001-999 32") is True  # с форматированием

    # Невалидные: неверный формат
    assert validate_snils("123") is False              # слишком короткий
    assert validate_snils("123456789012") is False     # слишком длинный
    assert validate_snils("abcdefghijk") is False      # не цифры

    # Невалидные: неверная контрольная сумма
    assert validate_snils("11223344500") is False