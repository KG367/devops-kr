from validator import validate_phone

def test_validate_phone_correct():
    assert validate_phone("+79991234567") is True

def test_validate_phone_incorrect():
    assert validate_phone("89991234567") is False