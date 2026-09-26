from validator import validate_email, validate_phone, validate_snils


def test_valid_phone():
    assert validate_phone("+7 999 123-45-67") is True
    assert validate_phone("89991234567") is True


def test_invalid_phone():
    assert validate_phone("123") is False
    assert validate_phone("abc") is False


def test_valid_snils():
    assert validate_snils("123-456-789 00") is True


def test_invalid_snils():
    assert validate_snils("123") is False