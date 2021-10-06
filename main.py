import uuid
import datetime

from flask import Flask, request, jsonify

app = Flask(__name__)

storage = {} 

@app.route("/note")
def getAllNotes():
    return jsonify(list(storage.values())), 200

@app.route("/note/<noteId>")
def getNote(noteId):
    if note := storage.get(noteId):
        return note
    return "Error!", 406

@app.route("/note", methods=["POST"])
def postNote():
    if content := request.json.get("content"):
        key = str(uuid.uuid4())
        time = datetime.datetime.utcnow().isoformat(sep='T', timespec='milliseconds') + 'Z'
        newNote = {"id": key, "created": time, "content": content}
        return jsonify(storage.setdefault(key, newNote)), 200
    return "Error!", 406

@app.route("/note/<noteId>", methods=["DELETE"])
def deleteNote(noteId):
    if noteId not in storage:
        return "Error!", 406
    del storage[noteId]
    return "OK", 200

if __name__ == "__main__":
    app.debug = True
    app.run()
