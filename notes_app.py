import json
from datetime import datetime

class Note:
    def __init__(self, id, title, text, date):
        self.id = id
        self.title = title
        self.text = text
        self.date = date

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'text': self.text,
            'date': self.date
        }
    @staticmethod
    def from_dict(note_dict):
        return Note(note_dict['id'], note_dict['title'], note_dict['text'], note_dict['date'])
    
class NotesApp:
    def __init__(self, file_path):
        self.file_path = file_path
        self.notes = self.load_notes()

    def load_notes(self):
        """Метод загрузки заметок"""
        try:
            with open(self.file_path, 'r') as file:
                notes_data = json.load(file)
                return [Note.from_dict(note) for note in notes_data]
        except FileNotFoundError:
            return []
        
    def save_notes(self):
        """Метод сохранения заметки"""
        with open(self.file_path, 'w') as file:
            json.dump([note.to_dict() for note in self.notes], file)

    def add_note(self, note):
        """Метод добавления заметки"""
        self.notes.append(note)
        self.save_notes()

    def read_notes(self, filter_date=None):
        """Метод чтения заметки"""
        if filter_date:
            filtered_notes = [note for note in self.notes if note.date.startswith(filter_date)]
            return filtered_notes
        return self.notes

    def edit_note(self, note_id, new_title, new_text):
        """Метод редактирования заметки"""
        for note in self.notes:
            if note.id == note_id:
                note.title = new_title
                note.text = new_text
                note.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.save_notes()
                break

    def delete_note(self, note_id):
        """Метод удаления заметки"""
        self.notes = [note for note in self.notes if note.id != note_id]
        self.save_notes()

if __name__ == '__main__':
    notes_app = NotesApp('notes.json')
    while True:
        print("1. Добавить новую запись")
        print("2. Просмотреть запись")
        print("3. Редактировать запись")
        print("4. Удалить запись")
        print("5. Выйти")

        choice = input("Ваш выбор: ")

        if choice == '1':
            id = input("Введите ID записи: ")
            title = input("Придумайте заголовок: ")
            text = input("Введите текст: ")
            date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            new_note = Note(id, title, text, date)
            notes_app.add_note(new_note)
            print("Запись добавлена!")

        elif choice == '2':
            filter_date = input("Введите дату записи в формате (yyyy-mm-dd HH:MM:SS) или оставьте поле пустым: ")
            filtered_notes = notes_app.read_notes(filter_date)
            for note in filtered_notes:
                print(f"{note.id}) {note.title}: {note.text} ({note.date})")

        elif choice == '3':
            note_id = input("Введите ID редактируемой записи: ")
            new_title = input("Введите новй заголовок: ")
            new_text = input("Введите новый текст: ")
            notes_app.edit_note(note_id, new_title, new_text)
            print("Запись отредактирована!")

        elif choice == '4':
            note_id = input("Введите ID удаляемой записи: ")
            notes_app.delete_note(note_id)
            print("Запись удалена!")

        elif choice == '5':
            print ("Вы вышли из приложения...")
            break

        else:
            print("Неправильный выбор. Попробуйте еще раз.")