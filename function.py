import operation_with_file
import Note
import view

number = 5  # Кол-во символов в заметке


def add():
    note = view.create_note(number)
    array = operation_with_file.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    operation_with_file.write_file(array, 'a')
    print('Заметка добавлена.')


def show(text):
    logic = True
    array = operation_with_file.read_file()
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            # logic = False
            print(Note.Note.map_note(notes))
        if text == 'id':
            # logic = False
            print('ID: ' + Note.Note.get_id(notes))
        if text == 'date':
            # logic = False
            if date in Note.Note.get_date(notes):
                print(Note.Note.map_note(notes))
            else: print(f'Увы.. Заметки от {date} не найдены.')


def id_edit_del_show(text):
    id = input('Введите ID  заметки: ')
    array = operation_with_file.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = view.create_note(number)
                Note.Note.set_title(notes, note.get_title())
                Note.Note.set_body(notes, note.get_body())
                Note.Note.set_date(notes)
                print(f'Заметка с ID {id} отредактирована.')
            if text == 'del':
                array.remove(notes)
                print(f'Заметка с ID {id} удалена.')
            if text == 'show':
                print(Note.Note.map_note(notes))
    if logic == True:
        print('Такой заметки не существует, проверьте коррестность ID')
    operation_with_file.write_file(array, 'a')