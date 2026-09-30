# tests/test_validator.py
from validator import validate_email, validate_phone


def test_validate_email():
    assert validate_email("test@example.com") == True
    assert validate_email("invalid") == False


def test_validate_phone_valid():
    assert validate_phone("+7 999 123-45-67") == True
    assert validate_phone("89991234567") == True
    assert validate_phone("8 (999) 123-45-67") == True


def test_validate_phone_invalid():
    assert validate_phone("12345") == False
    assert validate_phone("+1 555 123-45-67") == False
    assert validate_phone("abc") == False