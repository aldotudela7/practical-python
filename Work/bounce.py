# bounce.py
#
# Exercise 1.5
initial_height = 100
bounces = 1

while bounces <= 10:
    initial_height = round(initial_height*(3/5),4)
    print(bounces, initial_height)
    bounces+=1
