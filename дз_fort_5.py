import sqlite3

def connect():
    return sqlite3.connect('products.db')

def create_table():
    conn = connect()
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS products
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                quantity INTEGER NOT NULL)''')
    conn.commit()
    conn.close()

def add_product(name, price, quantity):
    conn = connect()
    c = conn.cursor()
    c.execute("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)", (name, price, quantity))
    conn.commit()
    conn.close()

def show_products():
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    rows = c.fetchall()
    conn.close()

    if rows:
        for row in rows:
            print(f"ID: {row[0]}, Название: {row[1]}, Цена: {row[2]}, Количество: {row[3]}")
    else:
        print("Нет продуктов в базе данных.")

def update_product(id, price, quantity):
    conn = connect()
    c = conn.cursor()
    c.execute("UPDATE products SET price = ?, quantity = ? WHERE id = ?", (price, quantity, id))
    conn.commit()
    conn.close()

def delete_product(id):
    conn = connect()
    c = conn.cursor()
    c.execute("DELETE FROM products WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def show_expensive_products():
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM products WHERE price > 2.0")
    rows = c.fetchall()
    conn.close()

    if rows:
        for row in rows:
            print(f"ID: {row[0]}, Название: {row[1]}, Цена: {row[2]}, Количество: {row[3]}")
    else:
        print("Нет продуктов с ценой выше 2.0.")

def get_product_by_id(product_id):
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM products WHERE id = ?", (product_id,))
    row = c.fetchone()
    conn.close()
    return row


def run_homework_tasks():
    print("=== Выполнение домашнего задания ===")
    
    
    add_product("Сахар", 1.9, 25)
    add_product("Масло", 3.2, 10)
    add_product("Сыр", 4.5, 15)
    print("Добавлены 3 новых продукта.")

    
    print("\nТовары с ценой выше 2.0:")
    show_expensive_products()


    product = get_product_by_id(3)
    if product:
        update_product(3, product[2], 35)
        print("\nОбновлено количество у продукта с ID = 3 до 35.")
    else:
        print("\nПродукт с ID = 3 не найден.")


    delete_product(4)
    print("Удалён продукт с ID = 4 (если существовал).")

    print("\nИтоговое состояние таблицы:")
    show_products()
    print("=== Домашнее задание выполнено ===\n")


def main():
    create_table()
    
    
    run_homework_tasks()

    while True:
        print("\nМеню:")
        print("1. Добавить продукт")
        print("2. Показать продукты")
        print("3. Обновить продукт")
        print("4. Удалить продукт")
        print("5. Показать товары дороже 2.0")
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            name = input("Введите название продукта: ")
            price = float(input("Введите цену продукта: ").replace(',', '.'))
            quantity = int(input("Введите количество продукта: "))
            add_product(name, price, quantity)

        elif choice == '2':
            show_products()

        elif choice == '3':
            id = int(input("Введите ID продукта для обновления: "))
            product = get_product_by_id(id)
            if product:
                price = float(input("Введите новую цену: ").replace(',', '.'))
                quantity = int(input("Введите новое количество: "))
                update_product(id, price, quantity)
            else:
                print("Продукт не найден.")

        elif choice == '4':
            id = int(input("Введите ID продукта для удаления: "))
            delete_product(id)

        elif choice == '5':
            show_expensive_products()

        elif choice == '6':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
