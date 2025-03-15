from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(name_and_number: str) -> str:
    """Функция возвращает маску номера карты ИЛИ счёта"""
    split_str = name_and_number.rsplit(' ', 1)  # Разделяем с права, чтобы отделить последний элемент
    card_type = split_str[0]
    number = int(split_str[1])

    if "Счет" in card_type:
        return f"Счет {str(get_mask_account(number))}"

    else:
        return f"{card_type} {str(get_mask_card_number(number))}"


print(mask_account_card("Счет 64686473678894779589"))

# def get_date(str) -> str:
# """Функция возвращает строку с датой в формате "ДД.ММ.ГГГГ" """
#
#     return str
