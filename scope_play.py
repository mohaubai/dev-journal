# from rich.console import Console

# console = Console()

# message = "I am global"

# def demo():
# 	message = "I am local"
# 	console.print(f"inside demo [orange]locals: {locals()}")
# 	console.print(f"global message still: {globals()['message']} ")

# demo()

food = "pizza"

def parents():
    food = "sushi"
    
    def my_room():
        #food = "burger"
        print(f"the food in my room is {food}")
    
    my_room()
    print(f"the food in my parents room is {food}")
    
parents()
print(f"The food in kitchen is {food}")