from random import *
main = ["spaghetti and meatballs", "lasagna", "cheeseburger", "pizza"]
sides = ["fries", "cole slaw", "rice", "salad"]
desserts = ["lava cake", "brownies", "icecream", "cheesecake"]
dinner = randint(0, len(main)-1)
dinner2 = randint(0, len(sides)-1)
dinner3 = randint(0, len(desserts)-1)
print("here's your dinner: ")
print("here's your main dish:",main[dinner])
print("here's your side dish:",sides[dinner2])
print("here's your dessert:", desserts[dinner3])
