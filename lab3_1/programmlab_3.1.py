# ФИО: Бобр Богдан Александрович
# Группа: ЦИБ-251
# Задание:  № 3.1.2 Дан список температурных изменений в течение дня (целые числа). Известно, что измеряющее устройство иногда сбоит и записывает отсутствие температуры (значение None ).


from typing import List, Optional


def parse_input(s: str) -> List[Optional[int]]:
    """
    Преобразует строку ввода в список температур.

    Поддерживает:
    - целые числа
    - значение None (как строка 'None')

    :param s: строка вида "1 2 None -3 5"
    :return: список [1, 2, None, -3, 5]
    :raises ValueError: если встречается некорректное значение
    """
    result: List[Optional[int]] = []
    for token in s.split():
        if token == "None":
            result.append(None)
        else:
            result.append(int(token))
    return result


def average_temperature(data: List[Optional[int]]) -> float:
    """
    Вычисляет среднюю температуру, игнорируя значения None.

    :param data: список температур
    :return: среднее значение
    :raises ValueError: если нет ни одного валидного измерения
    """
    valid = [x for x in data if x is not None]
    if not valid:
        raise ValueError("Нет корректных данных для вычисления среднего")
    return sum(valid) / len(valid)


def min_max_temperature(data: List[Optional[int]]) -> tuple[int, int]:
    """
    Находит минимальную и максимальную температуру, игнорируя None.

    :param data: список температур
    :return: (min, max)
    :raises ValueError: если нет валидных значений
    """
    valid = [x for x in data if x is not None]
    if not valid:
        raise ValueError("Нет корректных данных")
    return min(valid), max(valid)


def count_missing(data: List[Optional[int]]) -> int:
    """
    Подсчитывает количество пропущенных измерений (None).

    :param data: список температур
    :return: количество None
    """
    return sum(1 for x in data if x is None)


def main():
    """
    Основная функция: ввод, обработка и вывод результатов.
    """
    try:
        s = input().strip()
        data = parse_input(s)

        avg = average_temperature(data)
        mn, mx = min_max_temperature(data)
        missing = count_missing(data)

        print(f"Средняя температура: {avg:.2f}")
        print(f"Минимум: {mn}")
        print(f"Максимум: {mx}")
        print(f"Пропущено значений: {missing}")

    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
