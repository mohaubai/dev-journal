from rich.console import Console

console = Console()

message = "I am global"

def demo():
	message = "I am local"
	console.print(f"inside demo [orange]locals: {locals()}")
	console.print(f"global message still: {globals()['message']} ")

demo()
