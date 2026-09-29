# tests/test_validator.py
from validator import validate_phone

def test_validate_phone():
    assert validate_phone("+79161234567") is True
    assert validate_phone("89161234567") is False
