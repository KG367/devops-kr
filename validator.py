# validator.py
def validate_email(email: str) -> bool:
    """Валидация email-адреса."""
    import re
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))



def validate_phone(phone: str) -> bool:
    """Валидация российского номера телефона.

    Формат: +7XXXXXXXXXX или 8XXXXXXXXXX (11 цифр).
    """
    digits = ''.join(c for c in phone if c.isdigit())

    if len(digits) != 11:
        return False
    if digits[0] not in ('7', '8'):
        return False

    return True
# WIP: fix typo in phone validation docstring
