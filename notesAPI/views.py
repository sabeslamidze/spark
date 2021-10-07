from flask import Blueprint, request, jsonify
from .services import NotesManager

notes = Blueprint("notes", __name__)

storage = {} 
manager = NotesManager(storage)

@notes.route("/note")
def getAllNotes():
    try:
        return jsonify(manager.getAllNotes()), 200
    except Exception as e:
        return str(e), 500

@notes.route("/note/<string:noteId>")
def getNote(noteId):
    try:
        return jsonify(manager.getNote(noteId))
    except Exception as e:
        return str(e), 500

@notes.route("/note", methods=["POST"])
def postNote():
    try:
        content = request.json.get("content")
        return jsonify(manager.postNote(content)), 200
    except Exception as e:
        return str(e), 500

@notes.route("/note/<string:noteId>", methods=["DELETE"])
def deleteNote(noteId):
    try:
        manager.deleteNote(noteId)
        return "OK", 200
    except Exception as e:
        return str(e), 500 