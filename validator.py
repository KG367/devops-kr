# validator.py
def validate_email(email):
    """Проверка email."""
    return "@" in email and "." in email

def validate_phone(phone):
    """Проверка российского номера телефона."""
    return phone.startswith("+7") and len(phone) == 12
# WIP
