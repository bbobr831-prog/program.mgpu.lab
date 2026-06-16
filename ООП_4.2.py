# ==========================================
# БАЗОВЫЙ КЛАСС SERVICE (из ЛР 4.1)
# ==========================================

class Service:
    """Базовый класс IT-услуги."""

    def __init__(self, name, hourly_rate):
        # Название услуги
        self.name = name

        # Стоимость одного часа работы
        self.hourly_rate = hourly_rate

    def calculate_cost(self, hours):
        """
        Метод расчета стоимости.

        В базовом классе расчет обычный:
        стоимость = часы × цена за час
        """
        return hours * self.hourly_rate

    def __str__(self):
        """Красивый вывод объекта."""
        return (
            f"Услуга: {self.name} | "
            f"Стоимость/час: {self.hourly_rate} руб."
        )


# ==========================================
# ДОЧЕРНИЙ КЛАСС CONSULTING
# ==========================================

class Consulting(Service):
    """Консалтинговая услуга."""

    def __init__(self, name, hourly_rate, consultant):
        # Вызываем конструктор родительского класса
        super().__init__(name, hourly_rate)

        # Имя консультанта
        self.consultant = consultant

    def calculate_cost(self, hours):
        """
        Полиморфизм.

        Для консалтинга минимальное количество часов = 5.
        """

        # Если часов меньше 5, принудительно делаем 5
        if hours < 5:
            hours = 5

        return hours * self.hourly_rate

    def __str__(self):
        return (
            f"Консалтинг: {self.name} | "
            f"Консультант: {self.consultant}"
        )


# ==========================================
# ДОЧЕРНИЙ КЛАСС DEVELOPMENT
# ==========================================

class Development(Service):
    """Услуга разработки."""

    def __init__(self, name, hourly_rate, language):
        # Вызываем родительский конструктор
        super().__init__(name, hourly_rate)

        # Язык программирования
        self.language = language

    def calculate_cost(self, hours):
        """
        Для разработки стоимость считается стандартно.
        """

        return hours * self.hourly_rate

    def __str__(self):
        return (
            f"Разработка: {self.name} | "
            f"Язык: {self.language}"
        )


# ==========================================
# БАЗОВЫЙ КЛАСС CLIENT (из ЛР 4.1)
# ==========================================

class Client:
    """Базовый класс клиента."""

    def __init__(self, name, company):
        # Имя клиента
        self.name = name

        # Компания клиента
        self.company = company

    def __str__(self):
        return (
            f"Клиент: {self.name} | "
            f"Компания: {self.company}"
        )


# ==========================================
# ДОЧЕРНИЙ КЛАСС CORPORATECLIENT
# ==========================================

class CorporateClient(Client):
    """Корпоративный клиент."""

    def __init__(self, name, company, discount):
        # Инициализируем поля родителя
        super().__init__(name, company)

        # Корпоративная скидка
        self.discount = discount

    def __str__(self):
        return (
            f"Корпоративный клиент: {self.name} | "
            f"Скидка: {self.discount}%"
        )


# ==========================================
# КЛАСС-КОНТЕЙНЕР PROJECT
# ==========================================

class Project:
    """Проект, содержащий услуги."""

    def __init__(self, client):
        # Клиент проекта
        self.client = client

        # Пустой список услуг
        self.services = []

    def add_item(self, service):
        """
        Добавление услуги в проект.
        """

        self.services.append(service)

    def calculate_total(self, hours):
        """
        Итоговый расчет стоимости проекта.
        """

        # Начальная сумма
        total = 0

        # Перебираем все услуги
        for service in self.services:

            # Вызываем полиморфный метод calculate_cost()
            total += service.calculate_cost(hours)

        # Проверяем, является ли клиент корпоративным
        if isinstance(self.client, CorporateClient):

            # Применяем скидку
            total = total * (1 - self.client.discount / 100)

        return total


# ==========================================
# ОСНОВНАЯ ПРОГРАММА
# ==========================================

if __name__ == "__main__":

    # Создаем обычного клиента
    client1 = Client("Алексей", "TechSoft")

    # Создаем корпоративного клиента
    client2 = CorporateClient(
        "Мария",
        "Digital Group",
        10
    )

    # Создаем консалтинговую услугу
    service1 = Consulting(
        "IT-аудит",
        2000,
        "Иван Петров"
    )

    # Создаем услугу разработки
    service2 = Development(
        "Разработка сайта",
        3000,
        "Python"
    )

    # Создаем проект для корпоративного клиента
    project = Project(client2)

    # Добавляем услуги в проект
    project.add_item(service1)
    project.add_item(service2)

    # Выводим клиента
    print(client2)

    print()

    # Выводим услуги
    print(service1)
    print(service2)

    print()

    # Рассчитываем итоговую стоимость
    total_cost = project.calculate_total(3)

    # Вывод результата
    print(f"Итоговая стоимость проекта: {total_cost} руб.")