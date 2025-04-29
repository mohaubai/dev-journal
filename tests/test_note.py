from notes.note import Note
from notes.cli import add_note, list_notes

def test_snippet():
    n = Note('Hello', 'abcdefghijklmnopqrstuvwxyz')
    assert n.snippet() == 'abcdefghijklmnopqrst'

def test_list_notes_title(capfd):
    add_note("TestTile", "TestContent")
    list_notes()
    out, err = capfd.readouterr()
    assert "Title: TestTile" in out
