import uuid
import datetime

class NotesManager:
    def __init__(self, storage):
        self.storage = storage
    
    def getAllNotes(self):
        return list(self.storage.values())
    
    def getNote(self, noteId):
        if note := self.storage.get(noteId):
            return note
        raise Exception(f"Note with id {noteId} is not found!")

    def postNote(self, content):
        if not content:
            raise Exception("No content found!")
        key = str(uuid.uuid4())
        time = datetime.datetime.utcnow().isoformat(sep='T', timespec='milliseconds') + 'Z'
        newNote = {"id": key, "created": time, "content": content}
        return self.storage.setdefault(key, newNote).get("id")
    
    def deleteNote(self, noteId):
        if noteId not in self.storage:
            raise Exception(f"Note with id {noteId} is not found!")
        del self.storage[noteId]