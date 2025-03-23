def filter_by_state(transactions: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    """
    filtered_transactions = []  # Создаём пустой список для результата
    for transaction in transactions:  # Проходим по каждому словарю в списке
        if transaction.get('state') == state:  # Проверяем значение ключа 'state'
            filtered_transactions.append(transaction)  # Добавляем подходящий словарь в результат
    return filtered_transactions  # Возвращаем отфильтрованный список
