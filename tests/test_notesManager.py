import pytest

from notesAPI.services import NotesManager

@pytest.fixture
def manager():
    storage = {
        'b4408944-2c7f-448a-8268-e13d4df037a7': {
        'id': 'b4408944-2c7f-448a-8268-e13d4df037a7',
        'created': '2012-04-23T18:25:43.511Z',
        'content': 'This is a test note',
        },
    }

    return NotesManager(storage)


def test_getAllNotes(manager):
    notes = manager.getAllNotes()

    assert len(notes) == 1

def test_getNote(manager):
    note = manager.getNote('b4408944-2c7f-448a-8268-e13d4df037a7')

    assert note.get('id') == 'b4408944-2c7f-448a-8268-e13d4df037a7'
    assert note.get('created') == '2012-04-23T18:25:43.511Z'
    assert note.get('content') == 'This is a test note'

def test_getNotExistingNote(manager):
    with pytest.raises(Exception) as e:
        manager.getNote('invalidId')

        assert 'Note with id invalidId is not found!' in str(e.value)

def test_postNote(manager):
    newNoteId = manager.postNote('Test')

    assert newNoteId in manager.storage

def test_postNoteNoContent(manager):
    with pytest.raises(Exception) as e:
        manager.postNote('')

        assert 'No content found!' in str(e.value)

def test_deleteNote(manager):
    manager.deleteNote('b4408944-2c7f-448a-8268-e13d4df037a7')

    assert 'b4408944-2c7f-448a-8268-e13d4df037a7' not in manager.storage

def test_deleteNotExistingNote(manager):
    with pytest.raises(Exception) as e:
        manager.deleteNote('invalidId')

        assert 'Note with id invalidId is not found!' in str(e.value)