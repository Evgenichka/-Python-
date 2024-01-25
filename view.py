import Note


def create_note(number):
    title = check_len_text_input(
        input('Введите название заметки: '), number)
    body = check_len_text_input(
        input('Введите описание заметки: '), number)
    return Note.Note(title=title, body=body)


def menu():
    print("\nЭто приложение для заметок. Функционал приложения:"
    "\n\t1 - Вывод всех заметок из файла\n\t2 - Добавление заметки в файл"
    "\n\t3 - Удаление заметки из файла\n\t4 - Редактирование заметки\n\t5 - Выборка заметок по дате"
    "\n\t6 - Показать заметку по ID\n\t7 - Выход\n\nВведите номер функции: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов.\n')
        text = input('Введите текст: ')
    else:
        return text


def bye():
    print(f"Мы уже скучаем, возвращайтесь к нам скорее, {os.getlogin()}!")