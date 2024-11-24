'''
    Модуль в котором содержатся операции 
    добавления удаления поиска и вывода.
'''
import main

# Добавление книги
def add_book(library):
    title = input("Введите название книги: ").strip()
    author = input("Введите автора книги: ").strip()
    year = input("Введите год издания книги: ").strip()

    if not year.isdigit():
        print("Год издания должен быть числом.")
        return

    book = {
        "id": main.generate_id(library),
        "title": title,
        "author": author,
        "year": int(year),
        "status": "в наличии"
    }
    library.append(book)
    main.save_library(library)
    print("Книга успешно добавлена!")

# Удаление книги
def delete_book(library):
    try:
        book_id = int(input("Введите id книги для удаления: "))
    except ValueError:
        print("id должен быть числом.")
        return

    book = next((b for b in library if b["id"] == book_id), None)
    if not book:
        print("Книга с таким id не найдена.")
        return

    library.remove(book)
    main.save_library(library)
    print("Книга успешно удалена!")

# Поиск книги
def search_books(library):
    query = input("Введите Название книги, Автора или Год выпуска книги для поиска: ").strip()
    results = [
        book for book in library
        if query.lower() in str(book["title"]).lower() or
           query.lower() in str(book["author"]).lower() or
           query.lower() in str(book["year"])
    ]

    if results:
        print("Найдены следующие книги:")
        display_books(results)
    else:
        print("Книги по данному запросу не найдены.")

# Отображение всех книг
def display_books(library):
    if not library:
        print("Библиотека пуста.")
        return

    print("{:<5} {:<30} {:<20} {:<6} {:<10}".format("ID", "Название", "Автор", "Год", "Статус"))
    print("-" * 75)
    for book in library:
        print("{:<5} {:<30} {:<20} {:<6} {:<10}".format(
            book["id"], book["title"], book["author"], book["year"], book["status"]))

# Изменение статуса книги
def update_status(library):
    try:
        book_id = int(input("Введите id книги для изменения статуса: "))
    except ValueError:
        print("id должен быть числом.")
        return

    book = next((b for b in library if b["id"] == book_id), None)
    if not book:
        print("Книга с таким id не найдена.")
        return

    new_status = input("Введите новый статус (в наличии/выдана): ").strip()
    if new_status not in ["в наличии", "выдана"]:
        print("Некорректный статус. Допустимые значения: 'в наличии', 'выдана'.")
        return

    book["status"] = new_status
    main.save_library(library)
    print("Статус книги успешно обновлен!")