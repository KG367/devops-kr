# tests/test_validator.py

def test_validate_email():
    assert validate_email("test@example.com") == True
    assert validate_email("invalid") == False


def test_validate_phone_valid():
    assert validate_phone("+79161234567") == True
    assert validate_phone("89161234567") == True


def test_validate_phone_invalid():
    assert validate_phone("12345") == False
    assert validate_phone("+7abc") == False
    assert validate_phone("79161234567") == False
