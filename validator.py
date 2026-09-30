def validate_email(email: str) -> bool:
    """Валидация email-адреса."""
    import re
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))


def validate_phone(phone: str) -> bool:
    """Валидация российского номера телефона."""
    import re
    pattern = r'^\+?7\d{10}$'
    return bool(re.match(pattern, phone.replace('-', '').replace(' ', '')))


def validate_snils(snils: str) -> bool:
    """Валидация СНИЛС (Страховой номер индивидуального лицевого счёта).

    СНИЛС состоит из 11 цифр: 9 цифр номера + 2 цифры контрольного числа.
    """
    import re

    # Удаляем пробелы и дефисы для удобства ввода
    cleaned = snils.replace('-', '').replace(' ', '')

    # Проверка формата: ровно 11 цифр
    if not re.match(r'^\d{11}$', cleaned):
        return False

    # Первые 9 цифр — номер, последние 2 — контрольное число
    numbers = [int(digit) for digit in cleaned[:9]]
    check_sum = int(cleaned[9:11])

    # Расчёт контрольной суммы
    total = sum(d * (9 - i) for i, d in enumerate(numbers))

    if total < 100:
        expected = total
    elif total == 100 or total == 101:
        expected = 0
    else:
        remainder = total % 101
        if remainder < 100:
            expected = remainder
        else:
            expected = 0

    return check_sum == expected