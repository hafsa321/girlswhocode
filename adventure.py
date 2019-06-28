start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left.
'''

print(start)

print("Type 'left' or type 'right'") # Update to match your story.
user_input = input()
if user_input == "left":
    print("You decided to go left and you've escaped")
elif user_input == "right":
    print("You choose to go right but can still try and get out")

user2 = input("type up or down: ")
if user2 == "up":
    print("you've made the right choice and now you have one more challenge")
else:
    print("you got stuck again but can still try and get out")

user3 = input("type r or t: ")
if user3 == "r":
    print("you've made the right choice and now you've escaped")
else:
    print("you're stuck forever")
