import json
from datetime import datetime

class Note:
    def _init_(self, id, title, text, date):
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