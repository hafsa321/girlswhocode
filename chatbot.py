
# --- Define your functions below! ---

from random import *
# --- Put your main program below! ---
def main():
    i= 0
    while i < 1:
       main = ["spaghetti and meatballs", "lasagna", "cheeseburger", "pizza"]
       print("here are your options", main)
       answer = input("what would you like for dinner: ")
       print("here's your dinner:", answer)
       i += 1
       main()

#def desserts():
#    n=0
#    while n < 1:
#        desserts = ["lava cake", "brownies", "icecream", "cheesecake"]
#        print("here are your options", desserts)
#        answer2 = input("what would you like for dessert: ")
#        print("here's your dessert:", answer2)
#        i += 1
#        desserts()
# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
