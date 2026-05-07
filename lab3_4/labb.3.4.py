# ФИО: Бобр Богдан Александрович
# Группа: ЦИБ-251
# Задание:  № 3.4.2:  Дан файл, полученный на выходе задачи № 3.4.1:
 загрузите список чисел;
 вычислите их сумму и максимум и допишите их в файл.
#Выполнив программу несколько раз, убедитесь, что новые значения учитываются
#при подсчете.
#Если файл прочитать не удается, программа должна прекратить чтение и сообщить
#об этом пользователю.


#код к 3.4.1:
nums = input("Введите числа через пробел: ").split()

with open("numbers.txt", "w", encoding="utf-8") as file:
    for num in nums:
        file.write(num + "\n")

print("Данные записаны в файл")

#Код к 3.4.2:
try:
    with open("numbers.txt", "r", encoding="utf-8") as file:
        nums = [float(line.strip()) for line in file]

    total = sum(nums)
    maximum = max(nums)

    with open("numbers.txt", "a", encoding="utf-8") as file:
        file.write(f"{total}\n")
        file.write(f"{maximum}\n")

    print("Сумма:", total)
    print("Максимум:", maximum)

except FileNotFoundError:
    print("Не удалось прочитать файл")
