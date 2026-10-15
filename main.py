
from models import Calculator

calculator = Calculator()

while True:
    print("\n===== КАЛКУЛАТОР =====")
    print("1. Събиране")
    print("2. Изваждане")
    print("3. Умножение")
    print("4. Деление")
    print("5. Степенуване")
    print("6. История на операциите")
    print("7. Изчистване на историята")
    print("0. Изход")

    choice = input("Избери операция: ")

    if choice == "0":
        print("Довиждане!")
        break

    elif choice == "6":
        calculator.show_history()
        continue

    elif choice == "7":
        calculator.clear_history()
        continue

    elif choice in ("1", "2", "3", "4", "5"):
        try:
            a = float(input("Въведи първото число: "))
            b = float(input("Въведи второто число: "))

            if choice == "1":
                result = calculator.add(a, b)
            elif choice == "2":
                result = calculator.subtract(a, b)
            elif choice == "3":
                result = calculator.multiply(a, b)
            elif choice == "4":
                result = calculator.divide(a, b)
            else:
                result = calculator.power(a, b)

            print("Резултат:", result)

        except ValueError as error:
            print("Грешка:", error)

    else:
        print("Невалиден избор!")
