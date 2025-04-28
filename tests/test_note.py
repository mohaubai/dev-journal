from notes.note import Note

def test_snippet():
    n = Note('Hello', 'abcdefghijklmnopqrstuvwxyz')
    assert n.snippet() == 'abcdefghijklmnopqrst'
