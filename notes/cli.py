import argparse

notes = {}

def add_note(title, content):
    args = {'title': title, 'content': content}
    notes[title] = args
    print(f"Note '{title}' added.")
    return args

def list_notes():
    if not notes:
        print("No notes available.")
        return
    for title, note in notes.items():
        print(f"Title: {title}\nContent: {note['content']}\n")
    print("Notes listed.")
    return notes

def main():
    parser = argparse.ArgumentParser(description="Manage your notes.")
    subparsers = parser.add_subparsers(dest='command')

    subparsers.add_parser('add', help='Add a new note')
    subparsers.add_parser('list', help='list all notes')

    args = parser.parse_args()

    if args.command == 'add':
        title = input("Enter note title: ")
        content = input("Enter note content: ")
        add_note(title, content)
    elif args.command == 'list':
        list_notes()
    else:
        print("Invalid command. Use 'add' or 'list'.")
        exit(1)

if __name__ == "__main__":
    main()