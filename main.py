def add_note():
    # Спрашиваем текст у пользователя
    text = input("Напиши свою заметку: ")

    # Открываем файл в режиме добавления и пишем туда текст с переносом строки
    with open("notes.txt", "a", encoding="utf-8") as f:
        f.write(text + "\n")

    print("✅ Заметка сохранена!")


def show_notes():
    print("\n--- Твои заметки ---")

    # Открываем файл для чтения
    with open("notes.txt", "r", encoding="utf-8") as f:
        # readlines() читает файл и возвращает список строк
        lines = f.readlines()

        # Проверяем, пустой ли файл
        if len(lines) == 0:
            print("Заметок пока нет.")
        else:
            # Перебираем строки и выводим их с номерами
            for index, line in enumerate(lines):
                # line.strip() убирает невидимый перенос строки (\n) в конце
                print(f"{index + 1}. {line.strip()}")


print("--- Менеджер заметок ---")

while True:
    # Спрашиваем, что хочет сделать пользователь
    command = input(
        "\nВведи команду (add - добавить, show - показать, exit - выйти): ")

    if command == "add":
        add_note()
    elif command == "show":
        show_notes()
    elif command == "exit":
        print("Пока! Твои заметки сохранены.")
        break
    else:
        print("Неизвестная команда. Попробуй еще раз.")
