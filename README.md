# ed-task-widget-for-bank

Учебный проект по созданию виджета, который показывает несколько последних успешных банковских операций клиента.

## Описание

Проект состоит из следующих функций:

-   `get_mask_card_number(user_card_number: str) -> str`: Маскирует номер карты, показывая только первые 6 и последние 4 цифры.
-   `get_mask_account(user_account_number: str) -> str`: Маскирует номер счета, показывая только последние 4 цифры.
-   `mask_account_card(name_and_number: str) -> str`: Маскирует номера карты ИЛИ счёта
-   `get_date(date_iso_format: str) -> str`: Преобразование даты из формата iso в дд.мм.гггг
-   `filter_by_state(list_dict_info: List[Dict], state: str = "EXECUTED") -> List[Dict]`: Фильтрует список словарей на основе указанного параметра `state`.
-   `sort_by_date(list_dict: List[Dict], reverse: bool = True) -> List[Dict]`: Сортирует список словарей на основе ключа 'date'.

## Установка

Для установки и запуска проекта необходимо выполнить следующие шаги:

1.  **Клонируйте репозиторий:**

    ```
    git clone git@ghttps://github.com/GOrgONaPY/ed-task-widget-for-bank.git
    ```

2.  **Перейдите в папку проекта:**

    ```
    cd ed-task-widget-for-bank
    ```

3.  **Установите зависимости с помощью Poetry:**

    ```
    poetry install
    ```

## Использование

Примеры использования функций:

~~~
from src.widget import get_mask_card_number, get_mask_account, mask_account_card, get_date, filter_by_state, sort_by_date
from typing import Dict, List

Маскировка номера карты
card_number = "6831982470375048"
masked_card = get_mask_card_number(card_number)
print(f"Masked card number: {masked_card}") # Output: 6831 98** **** 5048

Маскировка номера счета
account_number = "12345678901234567890"
masked_account = get_mask_account(account_number)
print(f"Masked account number: {masked_account}") # Output: **7890

Маскировка информации о карте/счете
bank_details = "Visa Classic 6831982470375048"
masked_details = mask_account_card(bank_details)
print(f"Masked details: {masked_details}") # Output: Visa Classic 6831 98** **** 5048

Преобразование даты
date_string = "2023-10-26T00:00:00"
formatted_date = get_date(date_string)
print(f"Formatted date: {formatted_date}") # Output: 26.10.2023

Пример данных для фильтрации и сортировки
transactions: List[Dict] = [
{"id": 1, "date": "2023-10-27T10:00:00", "state": "EXECUTED", "amount": 100},
{"id": 2, "date": "2023-10-26T12:00:00", "state": "CANCELED", "amount": 50},
{"id": 3, "date": "2023-10-28T14:00:00", "state": "EXECUTED", "amount": 200},
]

Фильтрация по статусу
executed_transactions = filter_by_state(transactions, state="EXECUTED")
print(f"Executed transactions: {executed_transactions}")

Сортировка по дате
sorted_transactions = sort_by_date(transactions)
print(f"Sorted transactions: {sorted_transactions}")

~~~

## Зависимости

Проект использует следующие зависимости:

*   Python 3.13
*   Poetry (для управления зависимостями)


## Лицензия

Этот проект лицензирован по [лицензии MIT](LICENSE).
