from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(name_and_number: str) -> str:
    """Функция возвращает маску номера карты ИЛИ счёта"""
    split_str = name_and_number.rsplit(" ", 1)  # Разделяем справа, чтобы отделить последний элемент
    card_type = split_str[0]
    number = int(split_str[1])

    if "Счет" in card_type:
        return f"Счет {str(get_mask_account(number))}"

    else:
        return f"{card_type} {str(get_mask_card_number(number))}"


def get_date(date_iso_format: str) -> str:
    """Функция возвращает строку с датой в формате "ДД.ММ.ГГГГ" из "2024-03-11T02:26:18.671407" """
    day = date_iso_format[8:10]
    month = date_iso_format[5:7]
    year = date_iso_format[0:4]

    return f"{day}.{month}.{year}"
