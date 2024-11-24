'''
 Консольное приложения на Python 
 для управления библиотекой книг.
'''
import json
import os
import operations


# Путь к файлу JSON для хранения данных
DATA_FILE = "store_library.json"

# Инициализация данных библиотеки
def initialize_library():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as file:
            json.dump([], file)

# Загрузка данных из JSON файла
def load_library():
    with open(DATA_FILE, "r") as file:
        return json.load(file)

# Сохранение данных в JSON файл
def save_library(library):
    with open(DATA_FILE, "w") as file:
        json.dump(library, file, indent=4)

# Генерация уникального id
def generate_id(library):
    if not library:
        return 1
    return max(book["id"] for book in library) + 1


def main():
    initialize_library()
    library = load_library()

    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выход")
        
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            operations.add_book(library)
        elif choice == "2":
            operations.delete_book(library)
        elif choice == "3":
            operations.search_books(library)
        elif choice == "4":
            operations.display_books(library)
        elif choice == "5":
            operations.update_status(library)
        elif choice == "6":
            print("Вы вышли из программы.До свидания!")
            break
        else:
            print("Некорректный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()
