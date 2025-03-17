#Инициализация данных
toys = {
    "от 1 года": [
        {"name": "Погремушка", "price": 200, "description": "Яркая погремушка для малышей"},
        {"name": "Мягкий кубик", "price": 350, "description": "Мягкий кубик с картинками"},
    ],
    "от 3 лет": [
        {"name": "Мяч", "price": 500, "description": "Резиновый мяч для игр"},
        {"name": "Машинка", "price": 300, "description": "Инерционная машинка"},
        {"name": "Кукольный домик", "price": 2500, "description": "Домик для кукол с мебелью"},
    ],
    "от 6 лет": [
        {"name": "Кукла", "price": 1200, "description": "Кукла с аксессуарами"},
        {"name": "Пазл", "price": 800, "description": "Пазл на 100 элементов"},
        {"name": "Конструктор", "price": 1500, "description": "Конструктор с деталями"},
    ],
    "от 12 лет": [
        {"name": "Набор для опытов", "price": 2000, "description": "Набор для химических экспериментов"},
        {"name": "Головоломка", "price": 700, "description": "Сложная головоломка из металла"},
    ],
}

purchase_history = []  # История покупок
age_categories = set(toys.keys())  # Уникальные возрастные категории

#Функция для отображения меню игрушек
def show_menu():
    print("\nДоступные игрушки:")
    for category, items in toys.items():
        print(f"\nКатегория: {category}")
        for idx, toy in enumerate(items, 1):
            print(f"  {idx}. {toy['name']} - {toy['price']} руб. ({toy['description']})")

#Функция для фильтрации игрушек по возрасту
def filter_toys_by_age(category):
    if category in toys:
        print(f"\nИгрушки в категории '{category}':")
        for idx, toy in enumerate(toys[category], 1):
            print(f"{idx}. {toy['name']} - {toy['price']} руб. ({toy['description']})")
    else:
        print("Категория не найдена.")

#Функция для пополнения баланса
def add_balance(balance):
    try:
        amount = int(input("Введите сумму для пополнения: "))
        if amount > 0:
            balance += amount
            print(f"Баланс успешно пополнен. Текущий баланс: {balance} руб.")
        else:
            print("Сумма должна быть больше 0.")
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите число.")
    return balance

#Функция для обработки покупки
def process_purchase(category, choice, balance):
    if category in toys and 0 < choice <= len(toys[category]):
        toy = toys[category][choice - 1]
        if balance >= toy["price"]:
            print(f"\nВы выбрали: {toy['name']} ({toy['description']})")
            balance -= toy["price"]
            print(f"Ваш остаток: {balance} руб.")
            purchase_history.append(toy)
            return balance
        else:
            print("\nНедостаточно средств. Пожалуйста, пополните баланс.")
            return balance
    else:
        print("\nНеверный выбор. Пожалуйста, выберите игрушку из меню.")
        return balance

#Основная функция программы
def toy_store():
    balance = 0
    while True:
        print("\nГлавное меню:")
        print("1. Показать все игрушки")
        print("2. Фильтровать игрушки по возрасту")
        print("3. Пополнить баланс")
        print("4. Показать историю покупок")
        print("0. Выйти")
        
        try:
            menu_choice = int(input("Выберите действие: "))
            if menu_choice == 0:
                print("\nСпасибо за использование нашего магазина! До свидания!")
                print("История ваших покупок:")
                for purchase in purchase_history:
                    print(f"- {purchase['name']} ({purchase['price']} руб.)")
                break
            elif menu_choice == 1:
                show_menu()
                try:
                    category = input("Введите возрастную категорию (например, 'от 3 лет'): ")
                    if category in toys:
                        filter_toys_by_age(category)
                        choice = int(input("Выберите игрушку (введите номер) или 0 для возврата: "))
                        if choice != 0:
                            balance = process_purchase(category, choice, balance)
                    else:
                        print("Категория не найдена.")
                except ValueError:
                    print("Ошибка ввода. Пожалуйста, введите номер игрушки.")
            elif menu_choice == 2:
                print("\nДоступные возрастные категории:", ", ".join(age_categories))
                category = input("Введите возрастную категорию для фильтрации: ")
                if category in toys:
                    filter_toys_by_age(category)
                    try:
                        choice = int(input("Выберите игрушку (введите номер) или 0 для возврата: "))
                        if choice != 0:
                            balance = process_purchase(category, choice, balance)
                    except ValueError:
                        print("Ошибка ввода. Пожалуйста, введите номер игрушки.")
                else:
                    print("Категория не найдена.")
            elif menu_choice == 3:
                balance = add_balance(balance)
            elif menu_choice == 4:
                if purchase_history:
                    print("\nИстория покупок:")
                    for purchase in purchase_history:
                        print(f"- {purchase['name']} ({purchase['price']} руб.)")
                else:
                    print("\nИстория покупок пуста.")
            else:
                print("\nНеверный выбор. Пожалуйста, выберите действие из меню.")
        except ValueError:
            print("\nОшибка ввода. Пожалуйста, введите число.")

if __name__ == "__main__":
    toy_store()