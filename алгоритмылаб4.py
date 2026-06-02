# Лабораторная работа по алгоритмизации №4
# Выполнил: Бобр Богдан, ЦИБ-251
# Задание №2: Напишите функцию get_sha256_hash(s), возвращающую SHA-256 хеш строки.

import hashlib

def get_sha256_hash(s: str) -> str:
    # Переводим строку в байты и вычисляем хэш (SHA-256)
    return hashlib.sha256(s.encode()).hexdigest()

# Вызов функции
print(get_sha256_hash("Python"))




