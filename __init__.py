from anki.utils import htmlToTextLine
from aqt import AnkiQt, gui_hooks
from .config import getUserOption


def history(line, note):
    fields = note.fields
    col = note.col
    model = note.note_type()
    sort_idx = model["sortf"]
    sort_field = fields.pop(sort_idx)
    fields = [field_content for field_content in fields if field_content]
    fields = [sort_field] + fields
    txt = htmlToTextLine(", ".join(fields))
    nb_char = getUserOption("Number of character")
    if len(txt) > nb_char:
        txt = txt[:nb_char] + "..."
    return txt
    

gui_hooks.addcards_will_add_history_entry.append(history)
