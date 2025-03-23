from datetime import datetime  # Импорт наверху файла


def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.
    """
    filtered_transactions = []  # Создаём пустой список для результата
    for transaction in transactions:  # Проходим по каждому словарю в списке
        if transaction.get("state") == state:  # Проверяем значение ключа 'state'
            filtered_transactions.append(transaction)  # Добавляем подходящий словарь в результат
    return filtered_transactions  # Возвращаем отфильтрованный список


def sort_by_date(transactions: list[dict], reverse: bool = True) -> list[dict]:
    """
    Сортирует список словарей по дате.
    """

    def get_date(transaction: dict) -> datetime:
        """
        Возвращает дату из словаря в виде объекта datetime.
        """
        return datetime.fromisoformat(transaction["date"])

    return sorted(
        transactions,
        key=get_date,  # Используем функцию get_date для ключа сортировки
        reverse=reverse,  # Порядок сортировки
    )
