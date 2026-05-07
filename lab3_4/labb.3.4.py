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