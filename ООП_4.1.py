class Service:
    """Класс IT-услуги."""

    def __init__(self, name, hourly_rate):
        """
        Конструктор класса Service.

        :param name: название услуги
        :param hourly_rate: стоимость услуги за час
        """
        self.name = name
        self.hourly_rate = hourly_rate

    def display_info(self):
        """Вывод информации об услуге."""
        print(f"Услуга: {self.name}")
        print(f"Стоимость за час: {self.hourly_rate} руб.")

    def __str__(self):
        """Строковое представление объекта."""
        return (
            f"Услуга: {self.name} | "
            f"Стоимость за час: {self.hourly_rate} руб."
        )


class Client:
    """Класс клиента IT-компании."""
    
    def __init__(self, name, company):
        """
        Конструктор класса Client.

        :param name: имя клиента
        :param company: название компании
        """
        self.name = name
        self.company = company

    def display_info(self):
        """Вывод информации о клиенте."""
        print(f"Имя клиента: {self.name}")
        print(f"Компания: {self.company}")

    def __str__(self):
        """Строковое представление объекта."""
        return (
            f"Клиент: {self.name} | "
            f"Компания: {self.company}"
        )


if __name__ == "__main__":
    # Создание объектов класса Service
    service1 = Service("Разработка сайта", 2500)
    service2 = Service("Настройка сервера", 3000)
    service3 = Service("Техническая поддержка", 1800)

    # Создание объектов класса Client
    client1 = Client("Алексей", "TechSoft")
    client2 = Client("Мария", "Digital Group")
    client3 = Client("Иван", "Web Solutions")

    # Вывод услуг
    print("Список IT-услуг:")
    print(service1)
    print(service2)
    print(service3)

    print()

    # Вывод клиентов
    print("Список клиентов:")
    print(client1)
    print(client2)
    print(client3)