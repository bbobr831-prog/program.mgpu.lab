import hashlib

def get_sha256_hash(s: str) -> str:
    # переводим строку в байты и вычисляем хэш (SHA-256)
    return hashlib.sha256(s.encode()).hexdigest()

# ВЫЗОВ ФУНКЦИИ
print(get_sha256_hash("Python"))