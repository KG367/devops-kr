import re


def validate_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def validate_phone(phone: str) -> bool:
    """Validate Russian phone number."""
    pattern = r'^(\+7|8)[\s\-]?\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}$'
    return bool(re.match(pattern, phone))


def validate_snils(snils: str) -> bool:
    """Validate SNILS number (from instructor branch)."""
    pattern = r'^\d{3}-\d{3}-\d{3}\s\d{2}$'
    return bool(re.match(pattern, snils))