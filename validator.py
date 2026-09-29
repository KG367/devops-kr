# validator.py
def validate_email(email):
    """Проверка email."""
    return "@" in email and "." in email

def validate_phone(phone):
    """Проверка российского номера телефона."""
    return phone.startswith("+7") and len(phone) == 12

def validate_email(email: str) -> bool:
    """Валидация email-адреса."""
    import re
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))
